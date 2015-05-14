#!/usr/bin/env python
#
# pwr fcn
#
def is_power(a,b):
    if ((a%b) == 0 and is_power(a/b, b)):
        return True
    elif (a / b) == b:
        return True
    else:
        return False
print("Is it a power of the other?")
print("With a = 8, b = 2, then it is ",is_power(8,2))
print("a = 27, b = 3, ", is_power(27,3))
print("a = 10, b = 2, ", is_power(10,2))
