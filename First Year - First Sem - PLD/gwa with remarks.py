
#Program 3
#November 30, 2023
#Montanez, Andrei Chayne D.

#This program will compute for the final grade of the user given, the inputs are the lecture and laboratory grade and remarks Pass or Fail.

#variable yes_or_no is initialized to be equal to YES for the loop to run. It will only appear when the user needs to re-enter the inputs
yes_or_no = "YES"

#Initialize laboratory percentage to 0.3 since it makes up 30 percent of the final grade. 0.3 is from, 30 divided by 100
#Initialize lecture percentage to 0.7 since it makes up 70 percent of the final grade. 0.7 is from, 70 divided by 100
#Initialize passing grade to 75.
laboratory_percentage = 0.3
lecture_percentage = 0.7
Passing_grade = 75

#While loop is used so as long as the input passes several conditions, it continues. And when it does not pass, the user will be asked if they want to re enter inputs.
while yes_or_no.upper() == "YES":

    #Asks user to input lecture and laboratory grade
    lecture_grade = input("Please enter your lecture grade: ")
    laboratory_grade = input("Please enter your laboratory grade: ")

    #First condition, input must be numeric since it is grades of laboratory and lecture grade.
    if lecture_grade.isnumeric() == True and laboratory_grade.isnumeric() == True:
        lecture_grade = int(lecture_grade)
        laboratory_grade = int(laboratory_grade)

        #Second condition, the input must not be greater than 100. There are no grades higher the a perfect score.
        if lecture_grade <= 100 and laboratory_grade <= 100:
            final_grade = int((laboratory_grade*laboratory_percentage)+(lecture_grade*lecture_percentage))

            #This is to check if the grade Passes. If the condition is true, it outputs pass, otherwise, failed.
            #To display grades and remarks.
            if final_grade >= 75:
                print("Your final grade is", final_grade,"\b, You Passed!")
                yes_or_no = "NO" #ends the while loop

            #Failed grade
            else:
                print("Your final grade is", final_grade,"\b, You Failed.")
                yes_or_no = "NO" #ends the while loop


        #Else of the second condition, if the number is greater than 100 it will be trapped here. Negative numbers are already trapped in the first condition as if you input a dash to represent a negative number, it catches it.
        #Asks user if they want to re-enter inputs. Same concept as the else of the first condition.
        else:
            yes_or_no = input("There are no such thing as a grade greater than 100. Re-enter grades? type \"yes\" to re-enter. ")

    #Else of the first condition. Asks if the user wants to re enter values. Yes or no. If entered anything besides yes, the program exits. method ".upper" is used so user can input in any case and still be accepted.
    else:
        yes_or_no = input("Seems like you entered a non numerical value or a negative number.Re-enter grades? type \"yes\" to re-enter. ")

