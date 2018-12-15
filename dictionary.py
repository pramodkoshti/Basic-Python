# dictionary in python is unordered, indexed and changable collection

#create dictionary 1

my_dict = {
			"employee" : "pramod",
			"post" : "engineer",
			"joined" : "2016"
		  }
print(my_dict)		  

# Create dictionary using dict() constructor

my_dict = dict(employee = "pramod", post = "engineer", joined = "2016")
print(my_dict)

# Access items of dictionary 1

print(my_dict['employee'])

# Access dictionary using get method

print(my_dict.get('employee'))

# Change items in dictionary

my_dict['employee'] = 'Pradeep'
print(my_dict)

# loop through dictionary keys

for x in my_dict:
	print(x)

# loop through dictionary values

for x in my_dict:
	print(my_dict[x])

# loop through dictionary values another way

for x in my_dict.values():
	print(x)

# loop through key and values

for x, y in my_dict.items():
	print(x,y)

# check if item exists in dictionary

if "employee" in my_dict:
	print("Exists")

# check if item not exists in dictionary

if "salary" not in my_dict:
	print("Not exists")

# Add items to dictionary

my_dict["brand"] = "solidworks"
print(my_dict)

# remove item from dictionary using pop

my_dict.pop("brand")
print(my_dict)

# remove item from dictionary using del()

del my_dict["employee"]
print(my_dict)

# remove last item from dictionary using popitem

my_dict.popitem()
print(my_dict)

# clear all items from dictionary

my_dict.clear()
print(my_dict)

# delete dictionary

del my_dict
# print(my_dict)
# above statement will raise error

# create dictionary using fromkeys()

x = ('k1','k2','k3')
y = 0
my_dict = dict.fromkeys(x,y)
print(my_dict)

# copy dictionary

my_dict1 = my_dict.copy()
print(my_dict1)

# return key value pair from dictionary : return tuple of each key value pair

print(my_dict.items())

# return list containing keys

print(my_dict.keys())

# setdefault() will set the default value of the key if exists else insert the new with default value specified
# below case k4 key is not present and default value is not specified so it will insert None
my_dict.setdefault("k4")
print(my_dict)

# update dictionary value using key by update() method

my_dict.update({"k4":"4"})
print(my_dict)

# return values from dictionary
print(my_dict.values())













































