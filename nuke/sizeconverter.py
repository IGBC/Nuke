
"""converts unitsstring to float (only works for bits and bytes"""
def sizeconverter(string):
	numstr = ""
	# For every char
	for char in string:
		# If char is can be int'ed 
		if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
			# Add char to a number string
			numstr += char
			# Remove first char from string, should always be this one
			string = string[1:]
		else:
			# Else we're in non numeric land, this is where the units should be
			# So leave this loop and proceed to the next section
			break

	# First float the numstr
	try:
		outnum = float(numstr)	
	except ValueError:
		#if the user inputed something useless like 1.2.4132..1
		outnum = None
	except:
		raise

	# Here the string should just contain unitland
	
	# First char should be the SI prefix
	prefix = ""
	if len(string) > 0:
		prefix = string[0]
	
	# Try to assign a power to the prefix if it is not found then power 0
	try:
		power = ["k","M","G","T","P","E","Z","Y"].index(prefix)+1
	except Exception:
		power = 0
	
	if power != 0:
		# Cut char off
		string = string[1:]

	#multiply the outnum to give the correct value
	if outnum:
		outnum *= pow(1024,power)

	return [outnum, power, string] # String only contains the unit at this point






	
		