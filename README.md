# LuceVM & Technical Prototype

This repository contains LuceVM, a self-contained virtual machine to facilitate web3 development using the python stack. LuceVM allows to compile, deploy and interact with Ethereum Smart Contracts from a Python environment in a seamless matter.

The repository also contains supporting content and documentation materials I use in the process of building the technical prototype of the LUCE infrastructure. At this point all content in this repository is primarly to facilite the implementation of my master thesis and not (yet) optimised for wider useage.

## Usage of LuceVM

* First make sure [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/) are installed
* Then clone the base folder from github and set up the VM as follows:

```bash
cd /desired/location/
git clone https://github.com/arnoan/LUCE.git
cd ./luce_vm 
vagrant up # start the VM
vagrant ssh # ssh into the VM
bash prepare_system.sh
source ./bashrc # refresh shell
bash run_servers_tmux.sh # Start the servers
```
Then interface with server from host system via `http://127.0.0.1:8888` with password `luce`.

