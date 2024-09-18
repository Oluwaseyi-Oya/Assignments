# 1 - A FUNCTION THAT PRINTS THE LAST DIGIT OF A NUMBER
import string
from symbol import return_stmt


def print_last_digit (number):
    last_digit = number % 10
    return last_digit
result = print_last_digit(12345)
print ("Last digit:", result)

print()
print()

# 2 - A FUNCTION THAT PRINTS NUMBERS FROM 1-100 SEPARATED BY A SPACE

def fizzbuzz():
    for num in range (1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print ("Fizzbuzz", end=" ")
        elif num % 3 == 0 or num % 5 == 0:
            print ("Fizz" or "Buzz", end=" ")
        else:
            print (num, end=" ")

fizzbuzz()

print()
print()

# 3- A PROGRAM THAT PRINTS THE ASCII ALPHABET, IN REVERSE ORDER,
# ALTERNATING BETWEEN UPPER AND LOWERCASE, NOT FOLLOWED BY A NEW LINE

for i in range (25, -1, -1):
   char = chr(i + 97) if i % 2 == 0 else chr (i + 65)
   print (char, end="")

print()
print()

# 4 - CONVERT DECIMAL TO BINARY, OCTAL AND HEXADECIMAL

def convert_to_binary_octal_hexadecimal(number):
    binary = bin(number)[2:]
    octal = oct(number)[2:]
    hexadecimal = hex(number)[2:]
    return binary, octal, hexadecimal

decimal_number = 42
binary, octal, hexadecimal = convert_to_binary_octal_hexadecimal(decimal_number)

print ("Decimal:", decimal_number)
print ("Binary:", binary)
print ("Octal:", octal)
print ("Hexadecimal:", hexadecimal)

print()
print()

# 5 - PYTHON PROGRAM TO FIND ASCII VALUE OF A CHARACTER

def get_ascii_value(character):
    ascii_value = ord(character)
    return ascii_value
char = 'S'
ascii_value = get_ascii_value(char)
print ("The ASCII value of", char, "is", ascii_value)

print()
print()

# 6 - CONVERT FULL STRINGS TO ASCII

def string_to_ascii(string):

    character_ascii_list = []
    character_ascii_string = ""

    for character in string:
        ascii_code = ord(character)
        character_ascii_list.append(ascii_code)
        character_ascii_string+=f"{ascii_code} "

    return character_ascii_string


string_to_ascii("Ayomide")


ay_ascii = string_to_ascii("Ayomide")

print(ay_ascii)
    # create a list to hold the result
    # loop through the characters of the string; get the ascii code and add it to the list
    # print the list