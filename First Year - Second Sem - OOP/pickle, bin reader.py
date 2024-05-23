#Lab Assignment No. 2  - No.2
#Programmed by:Montanez, Andrei Chayne D.
#Course, Year, and Section: BSCpE 1-3
#Instructor: Engineer Julius S. Cansino
#Date of Submission: March 24, 2024

#pickle for reading reading and loading binary file
import pickle

highest = 3
name_highest = ""

#retrieving of data
with open("students.bin", "rb") as student_file:
    while True:
        try:
            individual = pickle.load(student_file)
            for name, gwa in individual:
                if gwa < highest:
                    highest = gwa
                    name_highest = name
        except EOFError:  # End of file reached
            break

#displaying of higehest
print("Student with the highest GWA:", name_highest)
print("Highest GWA:", highest)
