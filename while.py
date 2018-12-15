# while loop in python

a = 0
while a < 5:
	print(a)
	a += 1

# while with break

while a < 5:
	print(a)
	if a == 3:
		break
	a += 1	

# while with continue

while a < 5:
	a += 1	
	if a == 2:
		continue
	print(a)		