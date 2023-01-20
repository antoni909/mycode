#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)


# CHALLENGE 01 - Continue writing the script listmethods/listmeth02.py so that it demonstrates AT LEAST one of the methods found on https://docs.python.org/3/tutorial/datastructures.html0i

# remove all elements from a list
proto.clear()

# list comprehension to create lists based on some operation

squares = []
rangeOfTen = 10
for x in range(rangeOfTen):
    squares.append(x**2)

print(squares)

