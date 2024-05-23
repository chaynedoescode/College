#Lab Assignment No. 2  - No.3
#Programmed by:Montanez, Andrei Chayne D.
#Course, Year, and Section: BSCpE 1-3
#Instructor: Engineer Julius S. Cansino
#Date of Submission: March 24, 2024

#This program will write multiple line of text contents into a text file mylife.txt.

#opens and create a text file name mylife
mylife = open("mylife.txt","w")

#while true is used to allow user to input as many lines as they want
while True:
    line = input("Enter line: ")

    #adding the line to the text file
    mylife.write(line+"\n")
    again = input("Are there more lines y/n? ")

    #used lower to still allow user when they input "Y".
    #anything besides Y/y will be regarded as a no
    if again.lower() != "y":
        break

mylife.close()


