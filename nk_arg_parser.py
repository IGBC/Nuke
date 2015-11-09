import sys

class nukeArgParser:
	def __init__(self, parent=None):
		#we need a copy of this later, please don't ask hard questions
		self.argList = sys.argv

		# Set up storage
		self.filepath = ""
		self.bs = 32*1024*1024
		self.iterations = 3
		self.helpmsg = False
	#end

	#function that does everything
	def get(self):
		# Middle arguments should be flags and stuff
		# Look through the middle arguments to sort out flags, commands, and values.
		self.argParsed = [False] * (len(self.argList))

		for n in range(1, len(self.argList)) :
			self.parseArg(self.argList[n], n)

		#All arguments should have been read in by now, so lets process the data;

		if self.filepath == "" :
			self.helpmsg = True

		#if we need to show a help screen
		if self.helpmsg :
			return "HELP"
		else:
			return {"filepath": self.filepath,
					"blocksize": self.bs,
					"iterations": self.iterations}

	#end

	# Determines type of argument from text.
	def parseArg(self, arg, n):
		# if argument not dealt with then not expecting to be a value
		if self.argParsed[n] == False :
			
			
			#looks like a command or flag
			if arg[0] == "-":
				if arg[1] == "-":
					# starts with "--"
					self.commandTable(arg[2:], n)
				else:
					# starts with "-"
					self.flagParser(arg[1:], n)

			# Doesn't start with "-" so some sort of value that hasn't been caught yet. 
			# It's probably the filepath or the user is trolling us.
			else:
				# if we don't have a filepath yet stuff it in the filepath
				if self.filepath != "" :
					self.helpmsg = True
				else:
					self.filepath = arg
	#end


	# Looks up command from table
	def commandTable(self, arg, n):
		pass
	#end
	
	def flagParser(self, arg, n):
		for char in arg:
			if char == ("h" or "H"): self.helpmsg = True

			elif char == ("b" or "B"):
				try: self.bs = int(self.getNextVal(n))
				except ValueError :
					self.helpmsg = True

			elif char == ("i" or "I"):
				try: self.iterations = int(self.getNextVal(n))
				except ValueError :
					self.helpmsg = True
			
			else: self.helpmsg = True
	#end

	#finds next unprocessed value from argument after n
	def getNextVal(self, n):
		for i in range(n+1, len(self.argList)):
			if self.argParsed[i] == False :
				if self.argList[i][0] != "-" :
					self.argParsed[i] = True
					return self.argList[i]
				
				else :
					self.helpmsg = True
	#end