#Lab Assignment No 4: Problem No. 3
#Programmed by: Montanez, Andrei Chayne D.
#Course, Year and Section: BSCpE 1-3
#Instructor: Engr. Julius S. Cansino
#Date Submitted: April 20, 2024

#This program is an interactive calculator

#Custom Exception
class FormulaError(Exception):
    pass

#Accepted operations
operations = "+-/*"

print("Example — 1 + 1\n"
      "* / - +")
#while loop to allow user to input again
while True:
    #accepting input
    formula = input("Input Formula: ")
    #splitted into a list
    formula_splitted = formula.split()
    try:
        #checking number of indexes/elements and raising Formula error
        if len(formula_splitted) != 3:
            raise FormulaError
        else:
            #converting first and third element to float to check if they are numbers, raising ValueError as FormulaError
            formula_splitted_first = float(formula_splitted[0])
            formula_splitted_second = formula_splitted[1]
            formula_splitted_third = float(formula_splitted[2])
            #checking if operation is valid
            if formula_splitted_second not in operations:
                print('Use only "* / - +" operations')
                raise FormulaError
            #checking operation used
            else:
                if formula_splitted_second == "+":
                    answer = formula_splitted_first + formula_splitted_third
                elif formula_splitted_second == "-":
                    answer = formula_splitted_first - formula_splitted_third
                elif formula_splitted_second == "*":
                    answer = formula_splitted_first * formula_splitted_third
                else:
                    answer = formula_splitted_first / formula_splitted_third
    except (ValueError, FormulaError):
        print("FormulaError!")
    else:
        #displaying output and asking user if they want to quit the program.
        print(f"{formula} = {str(answer)}")
        print("Quit? y/n ", end = "")
        y_or_n = input("")
        if y_or_n.lower() != "n":
            break