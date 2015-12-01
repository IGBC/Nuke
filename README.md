# Nuke
## About
Nuke Is a light weight fast terminal appication for securly erasing hard disks. It addresses disks as files via the linux filesystem so can be used to effectively overwrite any block device or file.
## Usage
###Installation (The Quick and Dirty Way)
Clone / Download the repo

`cd` to the files

Run `sudo ./nuke/nuke.py`

###Installation (The Right Way)
Clone / Download the repo

`cd` to the files

Run `python3 ./setup.py build` to build the module

Run `sudo python3 ./setup.py install` to install the module to the machine.
The module is registered as the `nuke` command

###Running
This program can only access real hdd's as `root` as is normal with the linux permission system. Therefore run all commands below with `sudo` or as the root user.

####General Use
This shows all possible argument configurations
```nuke [-h][-u][-i iterations][-b blocksize] target```

####Default Use
```nuke /dev/sdb```
This will apply default aguments and run on `/dev/sdb`

####Arguments
Arguments can be in any order and grouped as follows `[-uib iterations blocksize]` or `[-biu blocksize iterations]`

`h` Print help and exit.

`i` Itterations of sucessive 0's and 1's to write to the target. \[Default 3\]

`b` Blocksize (in bytes) to use in each write batch (may effect performance, may not \[Default 32MB\]

##Licence
GPL V3.0 See licence file
