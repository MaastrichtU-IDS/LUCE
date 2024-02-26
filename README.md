# LUCE Technical Prototype

The paper is available online: https://arxiv.org/abs/2202.11646

The technical prototype of LUCE is accessible via LuceVM.

LuceVM is a self-contained virtual machine to facilitate web3 development. It encapsulates a Python-Django-Ethereum development stack and allows us to compile, deploy and interact with Ethereum Smart Contracts in a seamless manner. It was created primarily to facilitate the development of the LUCE technical prototype but can be used to support other blockchain-focused research as well.

This repository explains how to set-up LuceVM to access the LUCE Prototype.

## Online demo

Try the webhosted version:

* LUCE Web UI: https://luce.137.120.31.102.nip.io
* LUCE blockchain access: https://ganache.luce.137.120.31.102.nip.io

## Run with docker

Build

```bash
docker build -t vjaiman/luce .
```

Run

```bash
docker run -it -p 8000:8000 -p 8888:8888 vjaiman/luce
```

Run with docker-compose, the ganache DB and postgres DB will be stored in a `data` folder in the same directory as the `docker-compose.yml` file. You will need also to uncomment the ports in the `docker-compose.yml`

```bash
docker-compose up -d
```

> You can easily change the path to the storage folder by copying `.env.sample` to `.env` and change the storage path variable.

Access on http://localhost:8000 and connect with one of the demo account:

* provider@luce.com &nbsp; | provider
* requester@luce.com  | requester



## 🧑‍💻 Development setup

The final section of the README is for if you want to run the package in development, and get involved by making a code contribution.


### 📥️ Clone

Clone the repository:

```bash
git clone https://github.com/vemonet/luce
cd luce
```
### 🐣 Install dependencies

Install [Hatch](https://hatch.pypa.io), this will automatically handle virtual environments and make sure all dependencies are installed when you run a script in the project:

```bash
pip install --upgrade hatch
```

Install the dependencies in a local virtual environment:

```bash
hatch -v env create
```

### ☑️ Run tests

Make sure the existing tests still work by running ``pytest``. Note that any pull requests to the fairworkflows repository on github will automatically trigger running of the test suite;

```bash
hatch run test
```

To display all `print()`:

```bash
hatch run test -s
```

### 🧹 Code formatting

The code will be automatically formatted when you commit your changes using `pre-commit`. But you can also run the script to format the code yourself:

```
hatch run fmt
```

Check the code for errors, and if it is in accordance with the PEP8 style guide, by running `flake8` and `mypy`:

```
hatch run check
```

### ♻️ Reset the environment

In case you are facing issues with dependencies not updating properly you can easily reset the virtual environment with:

```bash
hatch env prune
```

# Difference with DecentralizedHealthcareBackend

LUCE uses their own python scripts in `utils/web3_scripts.py` with `web3` and `solc` to compile and publish 1 `utils/data/luce.sol` smart contract

DHB uses brownie to compile and publish many different smart contracts (luce registry, dataset, consent, plonk verifier for zkp)
