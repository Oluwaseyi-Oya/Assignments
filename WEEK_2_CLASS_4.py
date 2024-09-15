# 1- A PROGRAM TO CALCULATE THE FACTORIAL OF A NUMBER

num = int(input("Enter your number: "))
factorial = 1
i = 1

if num < 0:
    print ("factorial does not exist for negative number")
elif num == 0 or num == 1:
    print ("factorial is 1")
else:
    while i <= num:
        factorial = factorial*i
        i += 1
    print(f"factorial of {num} is this", factorial)

print()

# 2- RANGE TO COUNTDOWN FROM 5 TO 1

for x in range (5, 0, -1):
    print (x)
print ("Go!")

print()

# 3- RANGE TO COUNT DOWN FROM ZERO TO ONE AND COUNT UP FROM 4 TO 0

for x, y in zip (range (0, 5) , range (4, -1, -1)):
    print (x, y)

print()

# 4- REVERSE A WORD
name = "Oluwaseyi"
i = 0
l = len(name) - 1

while i <=l:
    print (name[l],end= " ")
    l = l - 1

print()
print()

# 5- FIRST 7 MULTIPLES OF 7

for i in range (1, 100):
    multiple = 7 * i
    if multiple > 49:
        break
    print (multiple, end = " ")

print()
print()

# 6- PRINT VOWELS IN THE SENTENCES
sentence = "The quick brown fox jumps over the lazy dog"
vowels = ["a", "e", "i", "o", "u"]

vowels_in_sentence = set()


for character in sentence:
    if character in vowels:
        vowels_in_sentence.add(character)
print()
print(f"Vowels in sentence are {vowels_in_sentence}")

print()
print()

# 7-  PRINT A 3D LIST
n = 3
numbers_in_3D = [[[0, 1, 2], [3, 4, 5], [6, 7, 8]], [[9, 10, 11], [12, 13, 14], [15, 16, 17]], [[18, 19, 20], [21, 22, 23], [24, 25, 26]]]
for row in numbers_in_3D:
    for num in row:
        print(num)