#!/usr/bin/env python3
import sys
import nk_arg_parser as parser
import nk_helper as helper
import os
import datetime
import random

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
	random = results["random"]

	#gallons and gallons of debug data
	#print("Filepath: " + filepath)
	#print("Blocksize: " + str(blocksize))
	#print("Iterations: " + str(iterations))

	print("Nuke will now erase ALL data on "+filepath+" including partitions and partition tables. All Data will be overwritten and irrecoverable.")
	print("Options Used:\n    Blocksize  = "+helper.sizeof_fmt(blocksize)+"\n    Iterations = "+str(iterations))
	if random:
		print("\n    Final pass will be pseudorandom data [WARNING: This is very slow]")

	confirm = input("\nAre you sure you wish to continue? [y/N]:")
	if (confirm != "y") and (confirm != "Y"):
		#program cancelled by user
		return 1
	# else we continue

	# Abitrary boobs (It's 10pm, and this isn't a cludge of hacks yet) (.)(.)

	# Get how big the filepath target is
	deviceSize = helper.get_file_size(filepath)
		

	# set what we're writing
	write = 0
	# repeat for number of iterations
	for i in range(1, iterations+1):
		# Get clear of the last output from writePass
		print("\n")
		print("Starting Pass "+ str(i))

		# Do a write pass
		# If final pass and random enabled
		if (i == iterations) and (random):
			# Make final pass random
			writePass(filepath, deviceSize, blocksize, "r")
		else:
			# Make a normal pass
			writePass(filepath, deviceSize, blocksize, write)
			write = 1-write #invert write 0 -> 1; 1 -> 0
	
	print()
	return 0
#end #if you are not me ignore these they make it easier to spot the end of highly indented functions


def writePass(filepath, size, blocksize, write):
	# Open our output file (write, binary) 
	outputFileH=open(filepath, mode="wb")
	# Jump to the start of the ouput file
	outputFileH.seek(0, 0)

	bytesWritten = 0
	bytesSinceUpdate = 0

	#timeing control
	startTime = datetime.datetime.now()
	lastUpdate = datetime.datetime.now()

	BpS = 0 #weird scope issue

	#get time for speed calculations
	now = datetime.datetime.now()

	# Flood it with our input data untill it begs us to stop,
	# ... using a valid safe word of course (well an IOError Execption).
	try:
		# This will flood the disk with data until the error fires. or we reach our disk size
		while bytesWritten < size:

			# Define input data for a 1, 0 or Random
			if write == 0 :
				# This generates a block of 0's the size of the blocksize by multiplying 1 byte by the blocksize
				inputData = b'\x00'*blocksize
			elif write == 1 :
				# This generates a block of 1's the size of the blocksize by multiplying 1 byte by the blocksize
				inputData = b'\xFF'*blocksize
			else:
				# Generate a random byte of data blocksize times
				# This is the weirdest line of python I have ever written
				inputData = bytearray(random.getrandbits(8) for _ in range(blocksize))

			#print(str(inputData))

			#write and count
			outputFileH.write(inputData)
			bytesWritten += blocksize
			bytesSinceUpdate += blocksize
			
			
			#get time for speed calculations
			now = datetime.datetime.now()
			
			#check if we updated recently
			if (now - lastUpdate) >= datetime.timedelta(seconds=1):
				shortElapsed = (now - lastUpdate).total_seconds()
				lastUpdate = now
				longElapsed = (now - startTime).total_seconds()
				

				#calculate B/s
				shortBpS = bytesSinceUpdate / shortElapsed
				bytesSinceUpdate = 0

				longBpS = bytesWritten / longElapsed

				#clear term line
				print(" "*96, end="\r")
				print("Written "+helper.sizeof_fmt(bytesWritten)+"/"+helper.sizeof_fmt(size)+" ["+helper.sizeof_fmt(longBpS)+"/s Avg] ["+helper.sizeof_fmt(shortBpS)+"/s Cur]", end="\r") 
	
	except IOError as e:
		pass
	finally:
		#print a final line else the output looks incomplete
		
		shortElapsed = (now - lastUpdate).total_seconds()
		lastUpdate = now
		longElapsed = (now - startTime).total_seconds()
		

		#calculate B/s
		shortBpS = bytesSinceUpdate / shortElapsed
		bytesSinceUpdate = 0

		longBpS = bytesWritten / longElapsed

		#clear term line
		print(" "*96, end="\r")
		print("Written "+helper.sizeof_fmt(bytesWritten)+"/"+helper.sizeof_fmt(size)+" ["+helper.sizeof_fmt(longBpS)+"/s Avg] ["+helper.sizeof_fmt(shortBpS)+"/s Avg]", end="\r")

		#close file
		outputFileH.close()	
		#flush IO buffers in the kernal
		os.sync()
#end

#entry point
if __name__ == "__main__" :
	sys.exit(main())
#end