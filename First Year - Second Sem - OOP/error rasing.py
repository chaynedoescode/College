#Lab Assignment No 4: Problem No. 4
#Programmed by: Montanez, Andrei Chayne D.:
#Course, Year and Section: BSCpE 1-3
#Instructor: Engr. Julius S. Cansino
#Date Submitted: April 20, 2024


def capitalize_last_name(name):
    try:
        #splits input into a list
        name_splitted = name.split()
        #traps input without exactly two names
        if len(name_splitted) != 2:
            raise ValueError("Seems like you entered more than 2 names. The program only excepts exactly two names.")
        else:
            #Checks if the name is alpha. Used or so it can only be unsatisfied when both are considered names
            if name_splitted[0].isalpha() == False or name_splitted[1].isalpha() == False:
                raise TypeError("Seems like you have made a Type Error, Please check your name.")
            else:
                #Uppercasing the first letter and lowercasing all the following
                #storing as first_name
                first_name = f'{name_splitted[0][0].upper()}{name_splitted[0][1:].lower()}'
                #Capitalizing the whole string
                #storing as last_name
                last_name = f'{name_splitted[1].upper()}'
    #Error Accepting
    except (ValueError, TypeError) as e:
        print(e)
    else:
        print(f'{first_name} {last_name}')

name = input("Please enter your first name and last name: ")
capitalize_last_name(name)
