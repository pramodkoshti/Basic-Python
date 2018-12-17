# File operations in python

#1 read existing file

f = open("demo.txt") # open("demo.txt","rt") can be used => r is for read mode and t stands for text file
print(f.read())

# read only part of the file
f = open("demo.txt","rt")

print(f.read(4))

# readline
f = open("demo.txt")
#using loop
for x in f:
	print(x)

# using readline function
f = open("demo.txt")
print(f.readline())	

# append line to existing demo.txt file = > creates the file if it doesn't exists

f = open("demo.txt", "a")
f.write("\nAppended new line")

# w is used to overrite the file content => create the file if doesn't exists

f = open("demo.txt","w")
f.write("All content of demo.txt file has been overwritten")

# open with x => create the file but gives error FileExistsError if already exists

f = open("demo.txt","x")


