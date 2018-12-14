# Python tuple
# It's unchangable collection
# Its Ordered collection


# tuples can be created by below ways

my_tuple = ("A","B","C")
print(my_tuple)

my_tuple = tuple(("A","B","C"))
print(my_tuple)

my_tuple = "A" ,"B"
print(my_tuple)

# for loop on tuple
for letter in my_tuple:
	print(letter)

# access index of item in tuple
print(my_tuple.index("A"))

# finding number of times item repeated in tuple
my_tuple = ("A","A","B","C")
print(my_tuple.count("A"))

# finding number of items in tuple
print(len(my_tuple))

# Checking if item exits in tuple
if "A" in my_tuple:
	print("A present in my_tuple")

# Checking if item not exist in tuple
if "D" not in my_tuple:
	print("D is not in my_tuple")	

# Get element from tuple using index
print(my_tuple[2])

# Concatinating two tuple
my_tuple1 = "A","B"
my_tuple2 = "C","D"
print(my_tuple1 + my_tuple2)

# Nested tuple
my_tuple3 = (my_tuple1,my_tuple2)
print(my_tuple3)

# tuple can be created by Repetition
my_tuple4 = ("A",)*3
print(my_tuple4)

# extract tuple items by index createria

my_tuple = ("A","B","C","D")

# Below statement will print all elements 
print(my_tuple[0:])

# Below statement will print elements from index 1 to index 2
print(my_tuple[1:3])

# Below Statement will reverse the tuple
print(my_tuple[::-1])

# though tuple is immutable we can delete it completely
del my_tuple
# Below line will give error
print(my_tuple)




























