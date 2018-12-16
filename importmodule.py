# import module: module.py is the file whose functions can be used in this scope

import module

module.display("Pramod")

print(module.module_dict["name"])


# there is another way just to import specific function or variable form modul

from module import module_dict
print(module_dict["age"])

# built in modules

import platform
print(platform.system())

# dir module can be used on any module to list down the functions and variables in the module

x = dir(module)
print(x)