"""
"" To take 
//: integer division, get the integer part of result
**: power, alos pow()
%: modulor
The star pass variable parameter as list, what difference not pass a list directly
*arg called unpacking operator
"""
def pythagorean(*arg):
    sum=0
    for x in arg:
        sum+=x**2
    return sum**(1/2)

test_data = [2,3,4]
# Unpacking, print the value
# the *arg means the parameter is in unpacked mode, 2,3,4 etc. So the arg is actually a tuple
print(*test_data)
print(pythagorean(2,3,4))
# ** unpacking key value dictionary
def concatenate(**kwargs):
    for key,value in kwargs.items():
        print(key, '->' , value)


concatenate(a="I", b="like",c="Pyhton")    
name = input("Please input your name: ")
print("your name is ",name)