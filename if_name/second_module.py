
# ANY FILE that ends in .py can be IMPORTED

# the name of the import matches the file name (minus the .py)
# these two files MUST BE IN THE SAME DIRECTORY

# __name__ is set to the name of the module being imported
# __name__ is set to the value __main__ on the module being RUN directly
# this makes it so that __name__ can be a conditional: is it being imported or being run directly

import first_module
first_module.main() # ADD THIS LINE
print("Module #2 Name=", __name__)

