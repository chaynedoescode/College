#Lab Assignment No. 2  - No.4
#Programmed by:Montanez, Andrei Chayne D.
#Course, Year, and Section: BSCpE 1-3
#Instructor: Engineer Julius S. Cansino
#Date of Submission: March 24, 2024

#This program will create two separate text files after reading the source text file named
#integers.txt that contains 20 integers

integer = open("integers.txt","r")

#temporary variables for storing numbers
even_list = []
odd_list = []

#for loop checks each line in the text file and checks if it's even or odd thru if-else statement
for number in integer:
    if int(number)%2 == 0:
        square = int(number)**2
        even_list.append(square)
    else:
        cube = int(number)**3
        odd_list.append(cube)

#Creating text files and data insertion
double = open("double.txt","w")
for square_num in even_list:
    double.write(str(square_num)+"\n")
double.close()
triple = open("triple.txt","w")
for cube_num in odd_list:
    triple.write(str(cube_num)+"\n")
triple.close()
integer.close()
