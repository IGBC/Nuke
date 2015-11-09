#!/usr/bin/env python3
import sys
import nk_arg_parser as parser
import nk_helper as helper
import os

def main():
	results = parser.nukeArgParser().get()
	# if argparser returned a help command
	if results == "HELP" :
		helper.printHelp()
		return 0
	
	# else run the program

	# fish out data from results dict
	filepath = results["filepath"]
	blocksize = results["blocksize"]
	iterations = results["iterations"]

	#gallons and gallons of debug data
	print("Filepath: " + filepath)
	print("Blocksize: " + str(blocksize))
	print("Iterations: " + str(iterations))

	# Abitrary boobs (It's 10pm, and this isn't a cludge of hacks yet) (.)(.)

	# Get how big the filepath target is
	deviceSize = helper.get_file_size(filepath)
		

	# set what we're writing
	write = 0
	# repeat for number of iterations
	for i in range(1, iterations+1):
		print("Writing Pass "+ str(i))
		# do a write pass
		writePass(filepath, deviceSize, blocksize, write)
		write = 1-write #invert write 0 -> 1; 1 -> 0
	return 0
#end #if you are not me ignore these they make it easier to spot the end of highly indented functions


def writePass(filepath, size, blocksize, write):
	# Define input data for a 1 or 0
	if write == 0 :
		inputData = b'\x00'*blocksize
	else :
		inputData = b'\xFF'*blocksize

	# Open our output file (write, binary) 
	outputFileH=open(filepath, mode="wb")
	# Jump to the start of the ouput file
	outputFileH.seek(0, 0)

	bytesWritten = 0

	# Flood it with our input data untill it begs us to stop,
	# ... using a valid safe word of course (well an IOError Execption).
	try:
		# This will flood the disk with data until the error fires. or we reach our disk size
		while bytesWritten < size:
			outputFileH.write(inputData)
			bytesWritten += blocksize
			# TODO: Text UI 
	except IOError as e:
		pass
	finally:
		#close file
		outputFileH.close()	
		#flush IO buffers in the kernal
		os.sync()
		#Let the user know we're not lazy
		print("Wrote " + helper.sizeof_fmt(bytesWritten))
#end

#entry point
if __name__ == "__main__" :
	sys.exit(main())
#end
