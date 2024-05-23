#Program 5
#January 3, 2023
#Montanez, Andrei Chayne D.

#This program will display sum of odd numbers, and sum of even numbers given X amount of inputs.

#First while loop allows user to input a new set of numbers
while True:
    #Ask user for how many input is expected
    #Error trapping negative, characters, and giving option to round the count
    while True:
        try:
            count_string = input("How many numbers are expected?  ")
            if count_string == "":
                yes_or_no = input("Please enter something. Type 'yes' to re-enter.  ")
                if yes_or_no.upper() != "YES":
                    exit()
            else:
                count = float(count_string)
                if count <= 0:
                    print("You can NOT input",count_string,"amount. Type 'yes' to re-enter.   ", end = "")
                    yes_or_no = input()
                    if yes_or_no.upper() != "YES":
                        exit()
                else:
                    if count_string.isdecimal() == False :
                        yes_or_no = input("You have entered a decimal. Type 'round' to round off and proceed. Type 'yes' to re-enter.   ")
                        if yes_or_no.upper() != "YES":
                            if yes_or_no.upper() != "ROUND":
                                exit()
                            else:
                                count = round(count)
                                break
                    else:
                        count = int(count_string)
                        break
        except ValueError:
            yes_or_no = input("Please enter only numerical values. Type 'yes' to re-enter.  ")
            if yes_or_no.upper() != "YES":
                exit()
    
    #For formality purposes
    def formality(count):
        count_str = str(count)
        if count_str == "11" or count_str=="12" or count_str=="13":
            formality = "th"
        elif count_str[-1] == "1":
            formality = "st"
        elif count_str[-1] == "2":
            formality = "nd"
        elif count_str[-1] == "3":
            formality = "rd"
        else:
            formality = "th"
        return formality
    
    #Trapping characters 
    def checker(actual_number):
        try:
            actual_float = float(actual_number)
            breaker = "True"
        except ValueError:
            yes_or_no =input("Please enter numerical values only. Type 'yes' to re-enter.  ")
            if yes_or_no.upper() != "YES":
                exit()
            else:
                breaker = "False"
        return breaker
    
    #Initializing a variable to store sum of each input.
    even_sum = 0
    odd_sum = 0
    
    #For individual formality and inputs.
    for individual in range(1, count+1):
        while True:
            formalities = formality(individual)
            print(str(individual)+formalities,"number:", end=" ")
            actual_number = input("")
            if actual_number == "":
                yes_or_no = input("Please enter something. Type 'yes' to re-enter. ")
                if yes_or_no.upper() != "YES":
                    exit()
            else:
                if checker(actual_number) == "True":
                    if float(actual_number)%2 == 0:
                        even_sum += float(actual_number)
                        break
                    else:
                        odd_sum += float(actual_number)
                        break
                    
    #To make sure if the output does not have a decimal, then it does not need to output the .0 at the end.
    even_str = str(even_sum)
    odd_str = str(odd_sum)
    if even_str[-1] == "0":
        even_str = int(even_sum)
    if odd_str[-1] == "0":
        odd_str =int(odd_sum)
    
    #Displaying of result
    print("")
    print("The sum of even numbers is", even_str)
    print("The sum of odd numbers is", odd_str)
    
    again = input("\nDo you wish to enter new set of numbers? Type 'yes' if you do. ")
    print("")
    if again.upper() != "YES":
        exit()
    