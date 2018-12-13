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

# del keyword removes specific index
del myList[0]
print(myList) 

# Clear items of list
myList.clear()
print(myList) 

# delete the list using del 
del myList

# print(myList) "This statement will generate error as list is deleted"






























