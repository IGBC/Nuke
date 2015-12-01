# Nuke Helper Functions.
import os
import sys

# This little hack deals with the fact that this program will be targeted
# ...at blk devices 90% of the time.
def get_file_size(filename):
	# Check File is actually a thing
	try:
		# Get the file size by seeking at end
		# Borrowed from http://stackoverflow.com/a/2774125
		fd = os.open(filename, os.O_RDONLY)
		try:
			return os.lseek(fd, 0, os.SEEK_END)
		finally:
			os.close(fd)
	except IOError as e:
		print("Error Reading \""+filename+"\"\nExiting.")
		# Exit with "Did Nothing"
		sys.exit(-1)
#end

# Open and print man page
def printHelp():
	print("\nNuke: Application for securely erasing drives")
	print("  Usage: nuke.py [-h][-u][-i iterations][-b blocksize] /path/to/target")
	print("    All information on the target device is overwritten with sucessive passes")
	print("    of 0’s and 1’s")
	print("\n  See man page for more information")
#end

# Returns the human readable version of a big number with SI Suffix
# Borrowed from http://stackoverflow.com/a/1094933
def sizeof_fmt(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Y', suffix)