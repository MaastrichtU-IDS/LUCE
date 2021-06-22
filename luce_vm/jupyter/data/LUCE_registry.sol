pragma solidity ^0.6.2;


pragma solidity ^0.6.2;

// Interface for LUCERegistry
interface LUCERegistryInterface {
    event newUserRegistered(address indexed user, uint license);
    
    function newDataProvider(address _provider) external;
    function checkProvider(address _provider) external view returns(bool);
    function registerNewUser(address newUser, uint license) external;
    function checkUser(address user) external returns(uint);
    function updateUserLicense(uint newLicense) external;
    function deregister() external;
}

contract ReducedLUCERegistry is LUCERegistryInterface {

    // This may be used for administrator control later. Not totally necessary. Can also remain unused.
    address public admin;

    // -------------------------------------- Provider section ---------------------------------------
    
    // Mapping for provider registration
    mapping (address => bool) public providerRegistry;
    
    /**
     * @dev Allows any person to register themselves as data provider.
     * @param _provider is the address of the new data provider to be registered. The function fails if
     * the _provider is already registered.
     */
    function newDataProvider(address _provider) external override {
        require(providerRegistry[_provider]==false, "This address is already registered as Provider.");
        providerRegistry[_provider] = true;
    }
    
    /**
     * @dev Allows any person to check whether a certain address belongs to a data provider.
     * @param _provider is the address of data provider in question.
     */
    function checkProvider(address _provider) external view override returns(bool) {
        return (providerRegistry[_provider]);
    }

    
    // -----------------------------------------User section -----------------------------------------
    
    // event newUserRegistered(address indexed user, uint license);
    
    // Maps the license of a data requester to their address. License 0 is default for all addresses, i.e. not registered.
    mapping (address => uint) public userRegistry;
    
    /**
     * @dev Allows (currently any) person to register themselves with (currently any) license. This function should
     * introduce more stringent requirements etc. to make sure only authorized usage is allowed.
     * @param newUser is the address of the new user to be registered.
     * @param license is the license of the new user to be registered.
     */
    function registerNewUser(address newUser, uint license) external override {
        require(userRegistry[newUser] == 0, "User is already registered.");
        userRegistry[newUser] = license;
        emit newUserRegistered(newUser, license);
    }

    /**
     * @dev Returns the license of a user. Not completely necessary, since the mapping is public.
     * @param user is the address of the user whose license is in question.
     */
    function checkUser(address user) external override returns(uint) {
        return (userRegistry[user]);
    }
    
    /**
     * @dev Allows any registered user to change their license. This should be controlled by the supervising authority
     * but such control is not yet implemented and not necessarily a good idea because centralized control defeats the
     * purpose of a decentralized ledger.
     * @param newLicense is the new license to be associated with the address of the msg.sender.
     */
    function updateUserLicense(uint newLicense) external override {
        require(userRegistry[msg.sender] != 0, "User is not yet registered.");
        userRegistry[msg.sender] = newLicense;
    }
    
    /**
     * @dev Allows a user to deregister themselves.
     */
    function deregister() external override {
        userRegistry[msg.sender] = 0;
    }

    constructor() public override {
        admin = msg.sender;
    }
}


contract LUCERegistry {

    // This may be used for administrator control later. Not totally necessary. Can also remain unused.
    address public admin;

    // -------------------------------------- Provider section ---------------------------------------
    
    // Data Provider Structs
    struct Provider {
        address[] contractAddress; // should these be arrays to enable multiple datasets per provider?
        string[] dataDescription;
        string[] link;
        uint[] requiredLicense;
    }
    
    // Mapping for provider registration
    mapping (address => bool) public providerRegistry;
    mapping (address => uint) private datasetsPerProvider;
    
    // Mapping for provider datasets
    mapping (address => Provider) private allDatasets;
    mapping (address => uint) private contractAllocation;
    
    address[] public providerAddresses;
    
    /**
     * @dev Allows any person to register themselves as data provider.
     * @param _provider is the address of the new data provider to be registered. The function fails if
     * the _provider is already registered.
     */
    function newDataProvider(address _provider) public {
        require(providerRegistry[_provider]==false, "This address is already registered as Provider.");
        providerRegistry[_provider] = true;
    }
    
    /**
     * @dev Allows any person to check whether a certain address belongs to a data provider.
     * @param _provider is the address of data provider in question.
     */
    function checkProvider(address _provider) public view returns(bool) {
        return (providerRegistry[_provider]);
    }
    
    /**
     * @dev Lists a new dataset in the allDatasets private mapping. 
     * @param _provider is the address of data provider publishing their dataset.
     * @param _contractAddress is the address of the associated smart contract.
     * @param _dataDescription is the description of the dataset.
     * @param _link is the link to the dataset.
     */
    function listNewDataset(address _provider, address _contractAddress, string calldata _dataDescription, string calldata _link, uint _requiredLicense) external {
        // This require is mostly redundant, since a malicious user could easily construct a contract with the same interface etc, but very different goals.
        require(msg.sender == _contractAddress, "Listing a dataset is not authorized by non-contract entitiy."); 
        datasetsPerProvider[_provider] += 1;
        contractAllocation[_contractAddress] = datasetsPerProvider[_provider];
        allDatasets[_provider].contractAddress.push(_contractAddress);
        allDatasets[_provider].dataDescription.push(_dataDescription);
        allDatasets[_provider].link.push(_link);
        allDatasets[_provider].requiredLicense.push(_requiredLicense);
        providerAddresses.push(_provider);
    }

    function updateDataset(address provider, uint contractNumber, string calldata updateDescr, string calldata newlink) external {
        address contractAddress = allDatasets[provider].contractAddress[contractNumber];
        require(msg.sender == contractAddress, "Update not authorized by non-contract entitiy.");
        allDatasets[provider].dataDescription[contractNumber] = updateDescr;
        allDatasets[provider].link[contractNumber] = newlink;
    }

    function updateDatasetLicense(address provider, uint contractNumber, uint newlicense) external {
        address contractAddress = allDatasets[provider].contractAddress[contractNumber];
        require(msg.sender == contractAddress, "Update not authorized by non-contract entitiy.");
        allDatasets[provider].requiredLicense[contractNumber] = newlicense;
    }

    /**
     * @dev Returns the public list of all data providers.
     */
    function getAllProviders() external view returns(address[] memory) {
        return providerAddresses;
    }
    
    function getProviderContractNumber(address _provider) external view returns (uint) {
        return datasetsPerProvider[_provider];
    }
    
    /**
     * @dev Returns the contract address and description of the dataset published by the _provider.
     * @param _provider is the address of data provider in question.
     */
    function getDatasetInfo(address _provider, uint _contractNumber) external view returns (address, string memory, uint) {
        require(_contractNumber <= datasetsPerProvider[_provider], "This provider has fewer datasets published than expected.");
        address contractAddress = allDatasets[_provider].contractAddress[_contractNumber-1];
        string memory dataDescription = allDatasets[_provider].dataDescription[_contractNumber-1];
        uint requiredLicense = allDatasets[_provider].requiredLicense[_contractNumber-1];
        return (contractAddress, dataDescription, requiredLicense);
    }

    
    // -----------------------------------------User section -----------------------------------------
    
    event newUserRegistered(address indexed user, uint license);
    
    // Maps the license of a data requester to their address. License 0 is default for all addresses, i.e. not registered.
    mapping (address => uint) public userRegistry;
    
    /**
     * @dev Allows (currently any) person to register themselves with (currently any) license. This function should
     * introduce more stringent requirements etc. to make sure only authorized usage is allowed.
     * @param newUser is the address of the new user to be registered.
     * @param license is the license of the new user to be registered.
     */
    function registerNewUser(address newUser, uint license) public {
        require(userRegistry[newUser] == 0, "User is already registered.");
        userRegistry[newUser] = license;
        emit newUserRegistered(newUser, license);
    }

    /**
     * @dev Returns the license of a user. Not completely necessary, since the mapping is public.
     * @param user is the address of the user whose license is in question.
     */
    function checkUser(address user) public view returns(uint) {
        return (userRegistry[user]);
    }
    
    /**
     * @dev Allows any registered user to change their license. This should be controlled by the supervising authority
     * but such control is not yet implemented and not necessarily a good idea because centralized control defeats the
     * purpose of a decentralized ledger.
     * @param newLicense is the new license to be associated with the address of the msg.sender.
     */
    function updateUserLicense(uint newLicense) public {
        require(userRegistry[msg.sender] != 0, "User is not yet registered.");
        userRegistry[msg.sender] = newLicense;
    }
    
    /**
     * @dev Allows a user to deregister themselves.
     */
    function deregister() public {
        userRegistry[msg.sender] = 0;
    }

    constructor() public {
        admin = msg.sender;
    }
}