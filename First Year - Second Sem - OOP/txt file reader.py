#Lab Assignment No. 2  - No.1
#Programmed by:Montanez, Andrei Chayne D.
#Course, Year, and Section: BSCpE 1-3
#Instructor: Engineer Julius S. Cansino
#Date of Submission: March 24, 2024

#This program will write a Python program that reads a text file named numbers.txt that
# contains 20 integers. The program will create two other text files; the first text file
# will be named even.txt that will contain  all  even  numbers  extracted  from  the
# numbers.txt.  The second  text  file  will  be  named  odd.txt  that  will  contain
# all  odd numbers extracted from the numbers.txt.

#reads source "numbers.txt" which contains numbers 1 through 20
numbers = open("numbers.txt", "r")

even = []
odd = []

#checking each line if it is even or odd
for num in numbers:
    num = num.strip()  # Remove whitespace
    if int(num) % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

#file creation
even_file = open("even.txt","w")
even_file.write(str(even)+"\n")
even_file.write("The number of even number is: "+str(len(even)))
even_file.close()

odd_file = open("odd.txt","w")
odd_file.write(str(odd)+"\n")
odd_file.write("The number of odd number is: "+str(len(odd)))
odd_file.close()

numbers.close()

