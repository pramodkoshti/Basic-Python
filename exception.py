# Exception in python

try:
	10 / 2
except ZeroDivisionError:
	print("You can't divide by zero")
except:
	print("Error unknown")	
else:
	print("else gets executed when try block gets executed without error")	
finally:
	print("Finally gets executed everytime")
	