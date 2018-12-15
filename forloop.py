# for loops in Python

list = ["A","B","C"]

for x in list:
	print(x)

# for loop with break

for x in list:
	if x == "C":
		break
	print(x)	

# for loop with  continue

for x in list:
	if x == "B":
		continue
	print(x)	

# for loop with range functionm

for x in range(10): # 10 will be values from 0 to 9
	print(x)

# range function with specifying limits

for x in range(10,20): # 10 to 19 as upper limit will be excluded
	print(x)

# range function with limits and increment parameter

for x in range(100,120,5): # 100 to 124 with increment of 5
	print(x)	

# else in for loop : code to execute after loop completion

for x in range(3):
	print(x)
else:
	print("Loop completed")

# nested loops

lis1 = ["A","B","C"]
list2 = ["D","E","F"]

for x in list:
	for y in list2:
		print(x,y)











