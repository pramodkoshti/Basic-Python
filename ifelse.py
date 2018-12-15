# if 

a= 10
b= 11
c= 12

if a < b:
	print("a is less than b")

# if else

if a > b:
	print("a is greater than b")
else:
	print("a is not greater than b")	

# nested if else

if a > b:
	print("a is greater than b")
elif b < c:
	print("b is less than c")
else:
	print("code which gets executed when none of the above condtion matches")

# short hand if

if a < b: print("a is less than b")

# short hand if else

print("a is less than b") if a < b else print("a is not greater than b") 

# if else with 3 conditions in one line

a = 10 
b = 10
c = 10
d = 11

print("A") if a > b else print("=") if a==b else "B"

# combining conditional statements

if a==b and b==c:
	print("a,b,c are equal")

if a==b or c=="d":
	print("c and d are not equal but a and b are")
	