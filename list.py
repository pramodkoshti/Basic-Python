#list in python is changable collection


#list intialisation
myList = ["Apple","Orange","Banana"]
print(myList)

# another way to create list using list() constructor
myList = list(("Apple","Orange","Banana"))
print(myList)

# Lets access ietms using index
print(myList[0])

# change ietm value using index
myList[0] = "kiwi"
print(myList)

# loop through the list
for x in myList:
	print(x)

# check if item exists
if "Orange" in myList:
	print("Orange is in myList")

# check if item does not exists
if "Mango" not in myList:
	print("Mango is not in myList")

# Get number of items in list
print(len(myList))	

# Append item to list
# It will add item at the end of the list
myList.append("Apple")
print(myList)

# Insert item at specific index
myList.insert(0,"Watermelon")
print(myList[0])

# remove specific item from list
myList.remove("Watermelon")
print(myList)

# Pop item from list

# if we don't specify the index then last item will Pop else specific item at index
myList.pop(0)
print(myList)

# get index of item
myList = ["Mumbai","Pune","Latur"] 
print("Mumbai is at position " + str(myList.index("Mumbai")))

# get how many times specific item repeat in list
myList = ["1","2","3","1"]
print("No of times '1' is repated is :", myList.count("1"))

# concatenation of list
myList1 = ["1", "2"]
myList2 = ["3","4"]
print(myList1 + myList2)

# create list using Repetition
myList1 = ["Mumbai",]*3
print(myList1)

# Nested list
myList1 = ["Orange","Mango"] 
myList2 = ["Apple","Kiwi"]
myList3 = [myList1,myList2]
print(myList3)

# extract items from list by index criteria
myList = ["A","B","C","D"]

# below code will print all items
print(myList[0:])

# below code will print items from index 1 to 2
print(myList[1:3])

# below code will reverse list
print(myList[::-1])

# del keyword removes specific index
del myList[0]
print(myList) 

# Clear items of list
myList.clear()
print(myList)

# delete the list using del 
del myList

# This statement will generate error as list is deleted
# print(myList)






























