# Nuke
## About
Nuke Is a light weight fast terminal appication for securly erasing hard disks. It addresses disks as files via the linux filesystem so can be used to effectively overwrite any block device or file.
## Usage
###Installation (The Quick and Dirty Way)
Clone / Download the repo
`cd` to the files
run `sudo ./nuke/nuke.py`

###Installation (The Right Way)
Clone / Download the repo
`cd` to the files
run `python3 ./setup.py build` to build the module
run `sudo python3 ./setup.py install` to install the module to the machine
The module is registered as the `nuke` command

###Running
```nuke.py [-h][-i iterations][-b blocksize] target```

Arguments can be in any order and grouped as follows `[-ib iterations blocksize] or [-bi blocksize iterations]`
####Arguments
`h` Print help and exit.

`i` Itterations of sucessive 0's and 1's to write to the target. \[Default 3\]

`b` Blocksize (in bytes) to use in each write batch (may effect performance, may not \[Default 32MB\]

##Licence
GPL V3.0 See licence file
