# lambda in python are annonymous functions

y = lambda x : x + 5

print(y(2))

# lambda with multiple args

z = lambda a,b : a + b
print(z(10,10))

# lambda functions can be used inside functions

def square_function(x):
	return lambda y : y * x

value_to_double = square_function(5)

print(value_to_double(5))	