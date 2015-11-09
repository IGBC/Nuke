# Nuke
## About
Nuke Is a light wieght fast terminal appication for securly erasing hard disks. It addresses disks as files via the linux filesystem so can be used to effectively overwrite any block device or file.
## Usage
###Installation (The Quick and Dirty Way)
Clone / Download the repo
`cd` to the files
run `sudo ./nuke.py` 
###Installation (The Right Way)
Something about paths and /usr/local/bin, If someone would like to tell me where the offically correct place to install python apps is then let me know and I'll make a proper launch script that can be linked into the path.

###Running
```nuke.py [-h][-i iterations][-b blocksize] target```
Arguments can be in any order and grouped as follows `[-ib iterations blocksize] or [-bi blocksize iterations]`
####Arguments
`h` Print help and exit.
`i` Itterations of sucessive 0's and 1's to write to the target. \[Default 3\]
`b` Blocksize (in bytes) to use in each write batch (may effect performance, may not \[Default 32MB\]

##Licence
GPL V3.0 See licence file
