#
# Example file for working with functions
#

# define a basic function
def func1():
    print("I am a function")


# function that takes arguments
def func2(arg1, arg2):
    print(arg1, "", arg2)

# function that returns a value
def cube(x):
    return x*x*x

# function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

#function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

# func1() #function gets called
# print(func1()) #function gets called inside print function however the function does not have return value so it returns None
# print(func1) #function doesnt get called, just prints the value of the function itself

# func2(10,20)
# print(func2(10,20))
# print(cube(3))
# print(power(2)) 
# print(power(2,3))
# print(power(x=3, num=2)) python arguments does not have to be in specific order

print(multi_add(4 ,2 , 5, 10 ,4 ,3)) # * sign means variable arguments