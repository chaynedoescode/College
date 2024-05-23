#Lab Assignment No 4: Problem No. 1
#Programmed by: Montanez, Andrei Chayne D.
#Course, Year and Section: BSCpE 1-3
#Instructor: Engr. Julius S. Cansino
#Date Submitted: April 20, 2024

#This program  prompts the user to enter a number, calculates its square root, and handles the 'ValueError'

#import math for squareroot
import math

#to check if the input is a number since next value error is for negative numbers only
def isnumber(num):
    try:
        float_num = float(num)
    except ValueError:
        print('You did not enter a number')
        exit()
    return

#writing file to sqrt_results.txt
with open('sqrt_results.txt','w') as results:

#while loop to let user add as many numbers as they want in the file
    while True:
        #ValueError traps squareroot of a negative number making it not able to proceed
        try:
            #input accepting
            number = input('Please enter a number: ')
            #using the function
            proceed = isnumber(number)
            #using math.sqrt from math library
            square_root = math.sqrt(float(number))
            results.write(str(square_root) + "\n")
            #asks user if they want to input another
            print('proceed? y/n ', end='')
            again = input('')
            #if "y" then input again, anyelse is trapped and break
            if again.lower() != "y":
                break
        except ValueError:
            print('You have entered a negative number.')
            break

results.close()