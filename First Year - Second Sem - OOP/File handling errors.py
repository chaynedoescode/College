#Lab Assignment No 4: Problem No. 2
#Programmed by: Montanez, Andrei Chayne D.
#Course, Year and Section: BSCpE 1-3
#Instructor: Engr. Julius S. Cansino
#Date Submitted: April 20, 2024

#This program reads the contents of a text file and implements error handling using try-except-finally block to handle exceptions  such as "FileNotFoundError" and "IOError".

def try_reading(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File contents:")
            print(content)
    #FileNotFoundError Trapped
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    #IOError Trapped
    except IOError:
        print("IOError occurred")
    finally:
        print("File handling completed.")

#Accepting name of file to search
filename = input("Example - alphabet.txt\n" 
                 "File name to find: ")
#Using the function to search the file
try_reading(filename)

