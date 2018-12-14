# set in python is unordered and unindexed collection

# set can be created using below ways
my_set = {"A","B","C"}
print(my_set)

my_set = set(("D","E","F"))
print(my_set)

# loop through set
my_set = set(("A","B","C","D","E","F"))
for x in my_set:
	print(x)

# check if item is in set
if "A" in my_set:
	print("A is in my_set")

# check if item is not in set
if "G" not in my_set:
	print("G is not in my_set")

""" set can't be changed but items can be added 
new item can be added at any position as its random"""
my_set.add("G")
print(my_set)

# Multiple items can be added at a time in set
my_set.update("H","I")
print(my_set)

# Get number of elements in set
print("Items in my_set are: " + str(len(my_set)))

# Items can be removed from set using two methods
#1 remove() method: This will raise an error if item is not present
print(my_set)
my_set.remove("H")
print(my_set)

#2 discard() method: This will not raise error if item is not present
print(my_set)
my_set.discard("G")
print(my_set)

"""remove last item in set using pop(): 
This method won't gurantee which item will be removed
as set are unordered in python"""
print(my_set)
my_set.pop()
print(my_set)

# copy set: it will return copy of the set
my_new_set = my_set.copy()
print(my_new_set)

# Difference between two sets:
# Below code will return elements which are in my_set_1 but not in my_set_2
my_set_1 = {"A","B","C"}
my_set_2 = {"A","D","F"}
print(my_set_1.difference(my_set_2))

# remove common items from my_set_1
my_set_1.difference_update(my_set_2)
print(my_set_1)

# intersection of two sets
my_set_1 = {"A","B"}
my_set_2 = {"A","B","C"}
my_set_3 = my_set_1.intersection(my_set_2)
print(my_set_3)

# intersection update: This will update intersecting elements in set
my_set_1 = {"A","B","D"}
my_set_2 = {"A","B","C"}
my_set_1.intersection_update(my_set_2)
print(my_set_1)

# isdisjoint(): returns true if both set have no intersecting element
my_set_1 = {"A","B"}
my_set_2 = {"C","D"}
z = my_set_1.isdisjoint(my_set_2)
print(z)

# issubset(): returns true if first set subset of second
my_set_1 = {"A","B"}
my_set_2 = {"C","D","A","B"}
z = my_set_1.issubset(my_set_2)
print(z)

# issuperset(): returns true if first subset have all elements in second set
my_set_1 = {"A","B","C","D"}
my_set_2 = {"C","D"}
z = my_set_1.issuperset(my_set_2)
print(z)

# symmetric_difference(): returns elements from both sets except the common ones
my_set_1 = {"A","B","C","D"}
my_set_2 = {"C","D"}
my_set_3 = my_set_1.symmetric_difference(my_set_2)
print(my_set_3)

# symmetric_difference_update(): This will update the first set with non intersecting elements from other
my_set_1 = {"A","B","C","D"}
my_set_2 = {"C","D"}
my_set_1.symmetric_difference_update(my_set_2)
print(my_set_1)

# union of two sets: union of all elements from both set 
my_set_1 = {"A","B","C","D"}
my_set_2 = {"C","D","E"}
my_set_3 = my_set_1.union(my_set_2)
print(my_set_3)

# update(): updates the first set with union of another set
my_set_1 = {"A","B","C","D"}
my_set_2 = {"C","D","E","F"}
my_set_1.update(my_set_2)
print(my_set_1)

# clear set
my_set_1.clear()
print(my_set_1)

# del set
del my_set_1
# below code will return error as set is deleted
# print(my_set_1)

















































































































