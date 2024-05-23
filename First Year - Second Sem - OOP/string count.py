#LAB ASSIGNMENT # 1 - Problem No. 4
#Programmed by: Montanez, Andrei Chayne D.
#Course, Year, and Section: BSCpE 1-3
#Instructor: Engineer Julius S. Cansino
#Date of Submission: March 9, 2024

#This program will ask the user to enter a string of any number of  characters.
# Then the  program  will outputon  the screen  the following count of characters
# based on the entered string

#initializing lists
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
numbers = "1234567890"

#accepting input and converting to lower for easier initializing
user_input = input("Input your string:  ")
user_input_lower = user_input.lower()

#initializing variables that will be used as counter
count_vowels = 0
count_consonant = 0
count_number = 0
count_special = 0
count_total = len(user_input)

#actual counting
for character in user_input_lower:
    if character in vowels:
        count_vowels += 1
    elif character in consonants:
        count_consonant += 1
    elif character in numbers:
        count_number += 1
    else:
        count_special +=1

#diplaying of result
print(f"""Number of vowels: {count_vowels}
Number of consonants: {count_consonant}
Number of digits: {count_number}
Number of Special Characters (including the spaces): {count_special}
Total number of characters found on the string: {count_total}""")


