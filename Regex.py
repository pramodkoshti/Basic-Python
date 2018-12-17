# Regex in Python
# We need to import the regex built in package for regex

import re

txt_sring = "Python is very easy!"

# In Python we have below functions 

# 1 search = > returns match object if there is a match

# regex to check if input start with Python or not 

result =  re.search("^Python",txt_sring)

if(result):
	print("Yes, input starts with Python")
else:
	print("No, input doesn't start with Python")


#2 findall => returns list cotaining all matches

result = re.findall("y",txt_sring)

print(result)

#3 split = > returns list of splitted items in string

result = re.split("\s",txt_sring)

print(result)

# sub => replaces string with specified characters

result = re.sub("\s","_",txt_sring)

print(result)

# Match object properties and methods

#1 span = > returns tuple of start and end postions of the match

result = re.search("^Python",txt_sring)
print(result.span())

#2 string = > returns string passed to function

print(result.string)

#3 group = > returns part of the string where you will have the match

print(result.group())