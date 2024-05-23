#LAB ASSIGNMENT # 1 - Problem No. 2
#Programmed by: Montanez, Andrei Chayne D.
#Course, Year, and Section: BSCpE 1-3
#Instructor: Engineer Julius S. Cansino
#Date of Submission: March 9, 2024

#This program will decrypt the message with corresponding vowels

#Dictionary giving the corresponding vowels with special characters respectfully
decrypter = {'*':'a', '&':'e', '#':'i', '+':'o', '!':'u'}

#Input accepting
user_input = input("Please enter a string to decode: ")

#preparing output
output_builder = ""

#for loop to check individual character
for character in user_input:
    if character in decrypter:
        output_builder += decrypter[character]
    else:
        output_builder += character

#displaying of output
print(output_builder)


