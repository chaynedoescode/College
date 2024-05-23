#Lab Assignment No 3: Problem No. 1
#Programmed by: Montanez, Andrei Chayne D.
#Course, Year and Section: BSCpE 1-3
#Instructor: Engr. Julius S. Cansino
#Date Submitted: April 06, 2024

#this function literally checks if a number is int or float. BUT is only used once the input is
#confirmed to be a number
def int_or_float(number):
    if "." in number:
        return float(number)
    else:
        return int(number)

#this checks if the input is a number. Since this is only used in the first input, I included
#to check if it is between 1 and 4. Made it a function for code readability
def isnumber(number):
    try:
        number_int = int(number)
        if number_int in range(1,5):
            operator = True
        else:
            print('Choose only from operations 1 to 4')
            print('Enter again? y/n ', end='')
            yes_or_no = input('')
            if yes_or_no.lower() != 'y':
                print('Thank you!')
                exit()
            else:
                operator = False
    #Traps non numerical numbers and floats since accepted inputs are only 1,2,3, and 4
    except ValueError:
        print('Please enter whole numerical values only')
        print('Enter again? y/n ', end= '')
        yes_or_no = input('')
        if yes_or_no.lower() != 'y':
            print('Thank you!')
            exit()
        else:
            operator = False

    return operator

#Made accepting two numbers from user a function to avoid repetitions of blocks of codes.
#The function also includes error trapping already
def number_input():
    while True:
        first_number = input('Please enter first number: ')
        second_number = input('Please enter second number: ')
        try:
            first_float = float(first_number)
            second_float = float(second_number)
            first_number = int_or_float(first_number)
            second_number = int_or_float(second_number)
            break
        except ValueError:
            print('Enter numerical values only. ')
            print('Enter again? y/n ', end='')
            yes_or_no = input('')
            if yes_or_no.lower() != "y":
                print('Thank you!')
                exit()

    return first_number, second_number

#print outside while loop to just be printed at the start
print('Welcome to Python Calculator!')

#while loop to allow user to input again
while True:
    print('Please choose one operation by typing the corresponding number\n')
    print('[1] Addition\n'
          '[2] Subtraction\n'
          '[3] Multiplication\n'
          '[4] Division\n')
    print('Enter your desired operation: ',end='')
    operation = input('')
    #first if-else checks if the user chose 1,2,3, or 4
    if isnumber(operation) == True:
        operation = int(operation)
        #Second if-else checks the chosen operator
        if operation == 1:
            print('first number + second number')
            first_number, second_number = number_input()
            sum = first_number + second_number
            print('The sum is: ',sum)

        elif operation == 2:
            print('first number - second number')
            first_number, second_number = number_input()
            difference = first_number - second_number
            print('The difference  is: ', difference)

        elif operation == 3:
            print('first number * second number')
            first_number, second_number = number_input()
            product = first_number * second_number
            print("The product is: ", product)

        else:
            #used while loop to trap zero division error and allow re-entering
            #re-entering after dividing since there is a loop already in the
            #function number_input()
            while True:
                print('first number / second number')
                first_number, second_number = number_input()
                try:
                    quotient =  first_number / second_number
                    print('The quotient is: ',quotient)
                    break
                except ZeroDivisionError:
                    print("ERROR!")
                    print('You tried to divide by zero. Enter again? y/n ', end = '')
                    yes_or_no = input('')
                    if yes_or_no.lower() != 'y':
                        print('Thank you!')
                        exit()
        # allows user to use the calculator again if needed.
        print('Do you want to use the calculator again? y/n ', end='')
        yes_or_no = input('')
        if yes_or_no.lower() != 'y':
            print('Thank you!')
            exit()