# functions in python

# parameter less function

def print_function():
	print("print_function is called")

# calling function
print_function()

# function with parameter

def function_with_paraneter(fname):
	print("Your name is " + fname)	

# calling function
function_with_paraneter('pramod')

# function with default parameter

def function_default_paraameter(name = 'pramod'):
	print("Your name is " + name)

# call above function without parameter

function_default_paraameter()

# function returning value

def retunr_function(a):
	return a *5

print(retunr_function(4))	