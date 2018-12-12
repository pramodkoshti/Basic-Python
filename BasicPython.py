#DOn't print this
"""Don't Print this as well"""
"""Don't Print this 
also"""
print("---Printitng Hello World---")
print("Hello World!")

print("---Indentation---")
if 1<2:
	print("One is Less Than two")

#Variables
print("---Variable output---")
x = 5
y = "Pramod"
print(x)
print(y)
print("---Output Variable---")	
x = "Python"
print("Welcome to " + x)
"""print("---Adding int and string---")
x = 5
y = "Python"
z = x + y
print(z)
print("Go On")"""
print("---Python Numbers---")	
x = 1
y = 1.1
z = 4j
print(x)
print("1 is of type int")
print(type(x))
print("1.1 is of type float")
print(type(y))
print("4j is of type complex")
print(type(z)) 
print("---Scientific Numbers---")	
x = 35e3
print("35e3")
print(x)
x = 35E4
print("35E4")
print(x)
x = 87.7e100
print("87.7e100")
print(x)
print("---complex Numbers---")
x= 3 +5j
print(x)
print("---Casting Numbers---")

x = int(1)
print(x)
x = int("2")
print(x)
x = int(2.2)
print(x)

x = float(1)
print(x)
x = float("2")
print(x)
x = float(4.3)
print(x)

x = str(15)
print(x)
x = str("Test")
print(x)
x = str(1.52)
print(x)


print("---Strings---")
print("Accessing first char of string 'Python' using [0] ")
x = "Python"
print(x[0])
print("Get the characters from position 2 to position 5 (not included) using [2:5]")
print(x[2:5])
x = ' Hello Python'
print("stripping leading and trailing white spaces from ' Hello Python '")
print(x.strip())
x = 'Python'
print("length of a string 'Python' using len()")
print(len(x))

print("upper() of 'Python'")
print(x.upper())

print("lower() of 'Python'")
print(x.lower())

print("replace() P in 'Python' with K")
print(x.replace("P","K"))

print("split() 'Hello, Python' by , seperator")
x = "Hello, Python"
print(x.split(','))

print("Command line input using input() function")
print("Enter Your Name")
x = input()
print("Your Name " +x)

















































