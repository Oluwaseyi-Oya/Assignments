# 1 - Write a function to calculate the square of a number. Document it properly using a docstring.
from math import factorial

def square_of_number(number):
    """
    calculates the square of a number

    parameter:
    number (int): The number to be squared

    return:
    int: The squared result
    """

    square = number * number
    return square
number = 7
result = square_of_number(number)
print (f"The square of {number} is {result}")

print ()

# 2 - Write a function calculator that contains two nested functions add and
# multiply to perform addition and multiplication on two numbers

def calculator (num1, num2):
    def add (x, y):
        return x * y
    def multiply (x, y):
        return x * y
    sum = add (num1, num2)
    product = multiply (num1, num2)
    return sum, product
num1 = 40
num2 = 15
result = calculator (num1, num2)
print ("sum:", result[0])
print ("product:", result[1])

print ()

# 3 - Create a lambda function that squares a number and apply it to a list using the map() function.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print (squared_numbers)

print()

# 4 - Write a recursive function to calculate the nth Fibonacci number

def fibonacci (n):
    if n <= 1:
        return n
    else:
        return fibonacci (n - 1) + fibonacci (n - 2)

n = 10
fibonacci_number = fibonacci(n)
print ("The", n, "th Fibonacci number is:", fibonacci_number)

print ()

# 5 - Use map(), filter(), and reduce() to:

# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
#
# doubled_numbers = list (map(lambda x: x * 2, numbers))
#
# odd_numbers = list (filter(lambda x: x % 2 != 0, doubled_numbers))
#
# product = reduce (lambda x, y: x * y, odd_numbers)
#
# print ("Doubled numbers:", doubled_numbers)
# print ("Odd numbers:", odd_numbers)
# print ("Product:", product)

print ()

# 6 - Write a function that accepts any number of positional and keyword arguments
def print_argument (*args, **kwargs):
    print ("positional arguments:", args)
    print ("number of positional argument:", len(args))
    print ("Keyword argument:", kwargs)
    print ("number of keyword argument:", kwargs)
    print ("total number of arguments:", len(args) + len(kwargs))

positional_argument = (1, 2, 3, 4, 5)
keyword_argument = {"name": "Mary", "age": "15"}
print_argument(*positional_argument, **keyword_argument)

print()

# 7 - Project: Build a Simple To-Do List

# 8 - Create a function describe_person() that takes positional and keyword arguments to describe a person.
def describe_person (*args, **kwargs):
    print ("positional arguments:", args)
    print ("keyword argument:", kwargs)

positional_argument = ("Joshua", "Adekoya")
keyword_argument = {"age": 54, "location": "Banana Island", "occupation": "Dentist"}
describe_person (*positional_argument, **keyword_argument)

print()

# 9 - ASSIGNMENT - WRITE THE FACTORIAL FUNCTION USING FOR/WHILE LOOPS
def num_factorial (n):
    if n < 0:
        return None

    factorial = 1
    i = 1
    while i <= n:
        factorial *= i
        i += 1
    return factorial

n = 7
result = num_factorial(n)
print (result)

