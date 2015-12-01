# Nuke
## About
Nuke Is a light weight fast terminal appication for securly erasing hard disks. It addresses disks as files via the linux filesystem so can be used to effectively overwrite any block device or file. Nuke has options to control the number of successive parses of 0's and 1's written to the disk. It also allows you to control the size of the blocks witten. 

Nuke can also fill the disk with random data when it has finished to remove evidence that the drive has been maliciously erased
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

`u` Random mode: Make the last itteration use random data. **WARNING:** This is *VERY* slow.

`b` Blocksize (in bytes) to use in each write batch (may effect performance, may not \[Default 32MB\]

####Recomended Argument Values
These values are recomended for best performance and security

From testing (S)ATA devices perform fastest with a blocksize of 32M (Default)

An itteration count of 3 (default) ensures that all bits on the device are flipped twice 0 -> 1 then 1 -> 0 which provides reasonable level of irrecoverability. 7 itterations of successive 0's and 1's is considered the military standard for data destruction. 7 is not the default as with any reasonably sized disk each pass takes several hours and for most purposes 7 passes is exessive. 

**NOTE FOR SOLID STATE DRIVES:**  

Solid State drives (including SSD's, SD cards, and USB Sticks) degrade when written to. The number of "write cycles" a device can survive before it fails can vary from a few thousand to a tens of millions. Nuke is very stressful to solid state drives. The repeated writing to the block device defeats the devices internal load balancing, and uniformly consumes a write cycle from the entire device. **Where security is not compromised use as few itterations as possible. DO NOT USE NUKE ON A SOLID STATE DRIVE FOR FUN**

Leave random mode off unless you have a use for it. Random mode is very slow (tested at ~3MB/s)

##Licence
GPL V3.0 See licence file
