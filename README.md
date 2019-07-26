# LuceVM & Technical Prototype

This repository contains LuceVM, a self-contained virtual machine to facilitate web3 development using the python stack. LuceVM allows to compile, deploy and interact with Ethereum Smart Contracts from a Python environment in a seamless manner.

The repository also contains supporting content and documentation materials I use in the process of building the technical prototype of the LUCE infrastructure. At this point all content in this repository is primarly to facilite the implementation of my master thesis and not (yet) optimised for wider useage.

## Usage of LuceVM

* First make sure [VirtualBox](https://www.virtualbox.org/) and [Vagrant](https://www.vagrantup.com/) are installed
  * On macOS High Sierra and Mojave the VirtualBox installation may fail
  * [This blog post](https://medium.com/@DMeechan/fixing-the-installation-failed-virtualbox-error-on-mac-high-sierra-7c421362b5b5) explains how to fix that
  * On Windows, ensure that [Hyper-V is enabled](https://www.vagrantup.com/docs/hyperv/)
* Check if `git` is installed and if not install from [here](https://git-scm.com)
  * To check if git is installed run `git --version` in the terminal 
  * If it is installed it will return the version number
* Then clone the LUCE base folder from github and set up the VM as follows:

```bash
cd ~/path/to/desired/location/
git clone https://github.com/arnoan/LUCE.git
cd ./LUCE/luce_vm 
vagrant up 								# start LuceVM
vagrant ssh -c 'bash start_servers.sh' 	# start the servers
```
Then access the Jupyter server from the host system via `http://127.0.0.1:8888` with password `luce`.  
(Or visit `http://127.0.0.1:4567` for further instructions.)

## Further Information

*Q: How do I stop the machine when I am finished working?*   
From within the same terminal where lucevm was started:
```
vagrant suspend
```
This hibernates the virtual machine. That way the next time it is started via `vagrant up` it will start much faster and be exactly in the same state again as you left off. There is no need to manually start the servers again.

*Q: How do I resume the machine?*   
No matter the state (hibernated, shut down, or not-yet-existing), we always use the same command to start it up:
```
vagrant up
```
If the machine was previously hibernated `vagrant up` is all that is needed. If the machine was shut down or completely destroyed the servers need to be manually started again with `vagrant ssh -c 'bash start_servers.sh'`.

*Q: How do I stop the machine completely?*   
The machine can be shut down completely via `vagrant halt` - in that case the servers have to be started again the next time LuceVM is booted. Finally `vagrant destroy` can be used to completely destroy the virtual machine instance. (The python notebooks are still preserved even if the machine is destroyed. That is because all application source code for Jupyter, Django, etc. actually lives on the host filesystem. It is automatically shared with the VM when a new machine instance is created.)

*Q: How can I update to the latest data contained in this github repository?*  
To update, first navigate to your local LUCE folder: `cd ~/path/to/LUCE/`  
Then run the following in the terminal:  
```bash
git fetch origin # this downloads all new content from github
git reset --hard origin/master # this replaces all local LUCE content with the newest updates
vagrant box update # this ensures you are using the latest lucevm and lucedb boxes
```

**Warning:** Note that by running `git reset` all LUCE files that may have been changed locally will be overwritten with the latest version from Github. In order to experiment locally with Jupyter notebooks without the possibility of them accidentally being over-written I created the `/jupyter/safe_storage_area/` folder. The contents of this folder are not synchronised with the github repository. Not even when `git reset` is executed. Please store all files you wish to keep safe in that folder.