

# py sets the __name__ to the string "main"
print(__name__)

# .py files are modules
#print("Module #1 Name=", __name__)
print("This code will always execute.")

def main():
    print("Module #1 Name=", __name__)

if __name__ == "__main__":
    #print("Code is being run directly from Python.")
    print("This code belongs to the main function in module 1.")
else:
    main()
    #print("Code is being run indirectly from import.")


