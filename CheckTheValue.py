"""
[ - Information About  Class - ]
Name class      : CheckTheValue
Version    		: 1.0.0
Version Python  : 3.4
functionality   : Check Of Value/s
Author			: Ayman Alaiwah
Fcaebook        : www.fb.com/ProgAymanAlaiwah
---------------------------------------------
[ - Contains these functions - ]
- isNumber
- isNegativeNumber
- isPositiveNumber
- isDecimalNumber
- isString
- isEmail
- isDate
----------------------------------------------
[ - Module Useding  At The Class ]
- [re] Default At Python
- [dateutil] Not Dufault At Python
  Must Working Install Modult Using Comand Line
	- Windows Or Any System
		 pip install python-dateutil 
	- Ubuntu Or Any System Linux Of Debian
		sudo apt-get install python-dateutil
-----------------------------------------------
"""
import re 
class CheckTheValue:
	# Name Function : Number Version 1.0.0
	# Function Number Working Of Checking are Check Of Value Number Positive Or Negative
	def isNumber(self,Number):
		pattern = r"^-?[0-9]+$"
		CheckNumber = re.match(pattern,str(Number))
		return CheckNumber

	# Name Function : isNegativeNumber Version 1.0.0
	# Function Number Working Of Checking are Check Of Value Number Negative
	def isNegativeNumber(self,Number):
		pattern = r"^-[0-9]+$"
		CheckNumber = re.match(pattern,str(Number))
		return CheckNumber

	# Name Function : isPositiveNumber Version 1.0.0
	# Function Number Working Of Checking are Check Of Value Number Positive
	def isPositiveNumber(self,Number,AddPlus = False):
		if AddPlus:pattern = r"^\+[0-9]+$"
		else:pattern = r"^[0-9]+$"
		CheckNumber = re.match(pattern,str(Number))
		return CheckNumber

	# Name Function : isDecimalNumber Version 1.0.0
	# Function isDecimalNumber Working Of Checking are Check Of Value If iDecimalNumber Or Not
	# If isDecimalNumber Return True Else Return False
	def isDecimalNumber(self,Number):
		pattern = "^[0-9]*\.[0-9]+$"
		CheckNumber = re.match(pattern,str(Number))
		return CheckNumber

	# Name Function : String Version 1.0.0
	# Function String Working Of Checking are Check Of Value If String Or Not
	# Content 2 Variable [ SpecialSymbols , CharacterStates ]
	# -[1] Variable SpecialSymbols Default Value Is Fasle This Is Variable Method are Permissible Content String ON Special Symbols
	# 	   If Value = False Not Permissible Special Symbols 
	#  [ Example 1 ] self.String('aymanAlaiwah','_|($^') OutPut = True
	#  [ Example 2 ] self.String('ayma|nA^laiw$ah','_|($^') OutPut = True
	# -[2] Variable CharacterStates Default Value Is Upper And Lwoer This Is Variable Method are Check Of Character States
	# 	   if lwoer String lwoer if upper String lwoer
	#  [ Example 1 ] self.isString('ayman','_|($^','lower') OutPut = True
	#  [ Example 2 ] self.isString('ayma|nA^laiw$ah','_|($^','Upper') OutPut = False
	#  [ Example 3 ] self.isString('ALAIWAH','_|($^','Upper') OutPut = True
	def isString(self,String, SpecialSymbols = False,CharacterStates = False):
		if str(CharacterStates).lower() == 'lower':
			CharacterStates = "a-z"
		elif  str(CharacterStates).lower() == 'upper':
			CharacterStates = "A-Z"
		else:
			CharacterStates = "a-zA-Z"

		if SpecialSymbols == False:
			SpecialSymbols = ""
		else:
			SpecialSymbols = list(SpecialSymbols)
			patternDeprecate = ['.','^','$','(',')','|','?']
			for i in range(len(SpecialSymbols)):
				if SpecialSymbols[i] in patternDeprecate:
						SpecialSymbols[i] = '\\'+SpecialSymbols[i]
			SpecialSymbols= "".join(SpecialSymbols)
		pattern = "^([{}]+|[{}]+)+([{}]|[{}])+$".format(SpecialSymbols,CharacterStates,SpecialSymbols,CharacterStates)
		CheckString = re.match(pattern,str(String))
		return CheckString

	# Name Function : Email Version 1.0.0
	# Function Email Working Of Checking are Check Of Value If Email Or Not
	# Content One Variable typeEmail Default All Type Email 
	# This Is Variable If Contant gmail Or htmail or Yahoo Or Any Type Email
		# -[2] Variable typeEmail 
	#  [ Example 1 ] self.isEmail('ayman@gmail.com') OutPut = True Any Type Email
	#  [ Example 2 ] self.isEmail('ayman2015@gmail.com','gmail') OutPut = True  Type Email Gmail
	#  [ Example 3 ] self.isEmail('ayman@gmail.com','yahoo') OutPut = False Type Email yahoo Email Not Email Yahoo Is Email gmail
	def isEmail(email,typeEmail = "[a-zA-Z0-9]+" ):
	    if typeEmail != '[a-zA-Z0-9]+':typeEmail = str(typeEmail).lower()
	    pattern = "^[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@{0}\.[a-zA-Z]+$".format(typeEmail)
	    CheckEmail = re.match(pattern, email)
	    return CheckEmail

	# Name Function : Date Version 1.0.0
	# Function Date Working Of Checking are Check Of Format If Date Or Not
	# Content One Variable formatDate Default [-] [- or / or any sompil ] DAY MOUNTH Year
	#  [ Example 1 ] self.isDate('10/2/1995') OutPut = True 
	def isDate(self,Date):
		try:
			from dateutil.parser import parse
		except:
			import os
			try:
				os.system("pip install python-dateutil")
			except:
				print("""
		Install Module [ dateutil ] Run Module On Python2 Or Python 3 
		- Windows Or Any System
			pip install python-dateutil
		- Ubuntu Or Any System Linux Of Debian
			sudo apt-get install python-dateutil
					""")
		try:
			parse(Date)
			return True
		except:
			return False
