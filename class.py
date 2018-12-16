# Python class

# declare class
class Employee:

	# declare cinstructor function 
	def __init__(emp, name,profile):
		# set variables
		emp.name = name
		emp.profile = profile
	
	# object method
	def display(emp):
		print("Welcome " + emp.name)

# create instance of Employee class
e1 = Employee('Pramod' , 'developer')

# retrieve class variables
print(e1.name)
print(e1.profile)	

# change class variables
e1.profile = "Designer"

print(e1.profile)

# delete object properties

del e1.profile

#below line will raise error as property has been deleted
# print(e1.profile)

# call object methods
e1.display()	


# delete class object
del e1

# below line will raise error as object has been deleted
#e1.display()