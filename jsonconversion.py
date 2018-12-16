import json

jsonobject = '{"name" : "Pramod","city" : "Pune","profile" : "developer"}'

# load json in python

json_to_python = json.loads(jsonobject)

print(json_to_python["name"]) 

# to convert from python to json we use dumps method

# Lets take python list to convert into json

list = ["A","B","C","D", "E"]

python_to_json = json.dumps(list)

print(python_to_json)

# use indent in dumps function to make output readable

print(json.dumps(list,indent =3))

# we can also use sort_keys= True : to get sorted results, separators= () : can be specified 