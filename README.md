# LuceVM & Technical Prototype

This repository contains LuceVM, a self-contained virtual machine to facilitate web3 development using the python stack. LuceVM allows to compile, deploy and interact with Ethereum Smart Contracts from a Python environment in a seamless manner.

The repository also contains supporting content and documentation materials I use in the process of building the technical prototype of the LUCE infrastructure. At this point all content in this repository is primarly to facilite the implementation of my master thesis and not (yet) optimised for wider useage.

## Usage of LuceVM

* First make sure [VirtualBox](https://www.virtualbox.org/) and [Vagrant](https://www.vagrantup.com/) are installed
  * On macOS High Sierra and Mojave the VirtualBox installation may fail
  * [This blog post](https://medium.com/@DMeechan/fixing-the-installation-failed-virtualbox-error-on-mac-high-sierra-7c421362b5b5) explains how to fix that
* Check if `git` is installed and if not install from [here](https://git-scm.com)
  * To check if git is installed run `git --version` in the terminal 
  * If it is installed it will return the version number
* Then clone the LUCE base folder from github and set up the VM as follows:

```bash
cd ~/path/to/desired/location/
git clone https://github.com/arnoan/LUCE.git
cd ./LUCE/luce_vm 
vagrant up # start the VM
vagrant ssh # ssh into the VM
bash prepare_system.sh
bash run_servers_tmux.sh # Start the servers
```
Then interface with server from host system via `http://127.0.0.1:8888` with password `luce`.

