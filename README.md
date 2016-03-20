# Nuke
## About
Nuke Is a light weight fast terminal appication for securly erasing hard disks. It addresses disks as files via the linux filesystem so can be used to effectively overwrite any block device or file. Nuke has options to control the number of successive parses of 0's and 1's written to the disk. It also allows you to control the size of the blocks witten.

Nuke can also fill the disk with random data when it has finished to remove evidence that the drive has been maliciously erased

## Important security notes
This program writes a series of successive passes of 1's and 0's over the target disk. As with most secure erasal programs the user has a choice of the number passes. A pass count of 3 (default) ensures that all bits on the device are flipped twice 0 -> 1 then 1 -> 0 which provides reasonable level of irrecoverability. 7 iterations of successive 0's and 1's is considered the military standard for data destruction. 7 is not the default as with any reasonably sized disk each pass takes several hours and for most purposes 7 passes is excessive.

Resent research into modern high density drives has shown that in cases one single overwrite pass to simply erase all the data is usually sufficent; using a pass of random data makes data recovery nearly impossible. Older forensic techniques to recover data from drives are impractical on high density devices.

#### Always note the following limitations of Nuke:
Nuke accesses the drive as if it were a file handle, and dumbly writes to it as such. Therefore if your storage medium abstracts it's complexity away from the host O/S (such as a zfs or btrfs disk pool*, or an array managed by a hardware RAID controller) then Nuke cannot guarantee that the entirety of the physical disk has been blanked, but that the entirety of the volume area presented to the O/S will have been written over. 

*In the case of a software managed raid the Nuke developer recomends running nuke seperately on each of the drives of the pool.

#### This application is not suitible for use on SSD's 
Solid state drives use hardware controllers to manage the very complex wear leveling, caching and NAND protection used in the device to maintain the very high performance and reliabilty they offer. Therefore Nuke can offer no better data protection than a standard disk format. SSD's provide a dedicated SATA function to flush all of their stored data safely and quickly (if you're curious it actually pulls all of the memory cells high and the electrons literally fall out of the memory cells) All nuke will do (like with a RAID array) is clear the volume area presented to the host O/S, repeated passes of writing to SSD's Like nuke performs can actually significantly reduce the lifespan of the device. **Don't use Nuke on SSD's.**




## Usage
### Installation (The Quick and Dirty Way)
Clone / Download the repo

`cd` to the files

Run `sudo ./nuke/nuke.py`

### Installation (The Right Way)
Clone / Download the repo

`cd` to the files

Run `python3 ./setup.py build` to build the module

Run `sudo python3 ./setup.py install` to install the module to the machine.

The module is registered as the `nuke` command

### Running
This program can only access real hdd's as `root` as is normal with the linux permission system. Therefore run all commands below with `sudo` or as the root user.

#### General Use
This shows all possible argument configurations

```nuke [-h][-u][-i iterations][-b blocksize] target```

#### Default Use
```nuke /dev/sdb```

This will apply default aguments and run on `/dev/sdb`

#### Arguments
Arguments can be in any order and grouped as follows `[-uib iterations blocksize]` or `[-biu blocksize iterations]`

`h` Print help and exit.

`i` Iterations of successive 0's and 1's to write to the target. \[Default 3\]

`u` Random mode: Make the last iteration use random data. **WARNING:** This is *VERY* slow.

`b` Blocksize (in bytes) to use in each write batch (may effect performance, may not \[Default 32MB\]

#### Recommended Argument Values
These values are recommended for best performance and security

Use an iteration count of 1-3 unless you are exceedingly paranoid.

From testing (S)ATA devices perform fastest with a blocksize of 32M (Default)

Use random mode only for very high security applications. Random mode is very slow (tested at ~3MB/s)

##Licence
GPL V3.0 See licence file
