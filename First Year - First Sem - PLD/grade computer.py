#Program 4
#Montanez_Andrei Chayne D.
#December 12, 2023

#This program will compute for the user's grade

#Numbers contain the characters that are expected to be used in the input.
numbers = "1234567890."
#Input validity checker.
    #variable "scores" is the input
    #function is used to make the program shorter in terms of lines
def valid(score):
    proceed = 0
    decimal_counter = 0
    #this if, checks first if the input is a number. or a negative number by using - sign.
    if score == "":
        print("Please enter a grade.")
    for char in score:
        if char not in numbers:
            yes_or_no = input("Your input was not a number or a negative number using \"-\". Type \"yes\" to re-enter. ")
            if yes_or_no.upper() != "YES":
                exit()
            else:
                proceed = 0
                break
        #This just checks how many decimal points are there in the input and counts them.
        if char == ".":
            decimal_counter += 1
        if decimal_counter > 1:
            yes_or_no = input("You input contained more than 1 decimal point. Type\"yes\" to re-enter. ")
            if yes_or_no.upper() !="YES":
                    exit()
            else:
                proceed = 0
                break
        else:
            proceed = 1
    if proceed == 1:
        if float(score) > 100:
            yes_or_no = input("You seemed to have entered a number greater than 100. Type \"yes\" to re-enter.  ")
            if yes_or_no.upper() != "YES":
                exit()
            else:
                proceed = 0
    return score, proceed
#will be used to check if the name is valid. space " " is included
letters = "qwertyuiopasdfghjklzxcvbnm QWERTYUIOPASDFGHJKLZXCVBNM"

#Asks for name input and checks if it is a name using "letters"
while True:
    name = input("What is your name?  ")
    if name == "":
        print("Please enter a name.")
        proceed = 0
    else:
        for char in name:
            if char not in letters:
                yes_or_no = input("Invalid input. Type \"yes\" to re-enter. ")
                if yes_or_no.upper() != "YES":
                    exit()
                else:
                    proceed = 0
                    break
            else:
                proceed = 1
    if proceed == 1:
        break

#Letting user know what to input
#Noticed I used "grade" since the input is expected to be a percentage and not a score like 45/50, in grade it is 90% or in this case. disregarding the %, 90.
print("\nLECTURE")
print("Enter grade only. For example 85, 90.8, 60"
      "\n"
      "Entered values are already in percentage form. Use of \"%\" is not necessary.")

#assigned proceed to 0 before every loop to not break out of it.
proceed = 0

#this while loop allows user to re-enter values incase of errors only in the specific component they made a mistake in
while True:
    lecture_quiz_input = input("Out of 100, please enter your QUIZ grade:   ")
    #assigning the return to two variables
    lecture_quiz_input, proceed = valid(lecture_quiz_input)
    if proceed == 1:
        break

#process repeats at every input
proceed = 0
while True:
    lecture_assignment_input = input("Out of 100, please enter your ASSIGNMENT grade:   ")
    lecture_assignment_input, proceed = valid(lecture_assignment_input)
    if proceed == 1:
        break

proceed = 0
while True:
    lecture_activities_input = input("Out of 100, please enter your ACTIVITY grade:   ")
    lecture_activities_input, proceed = valid(lecture_activities_input)
    if proceed == 1:
        break

proceed = 0
while True:
    lecture_project_input = input("Out of 100, please enter your PROJECT grade:   ")
    lecture_project_input, proceed = valid(lecture_project_input)
    if proceed == 1:
        break

proceed = 0
while True:
    lecture_recitation_input = input("Out of 100, please enter your RECITATION grade:   ")
    lecture_recitation_input, proceed = valid(lecture_recitation_input)
    if proceed == 1:
        break

proceed = 0
while True:
    lecture_midterms_input = input("Out of 100, please enter your MIDTERMS grade:   ")
    lecture_midterms_input, proceed = valid(lecture_midterms_input)
    if proceed == 1:
        break

proceed = 0
while True:
    lecture_finals_input = input("Out of 100, please enter your FINALS grade:   ")
    lecture_finals_input, proceed = valid(lecture_finals_input)
    if proceed == 1:
        break

print("\n"
      "LABORATORY")
proceed = 0
while True:
    laboratory_quiz_input = input("Out of 100, please enter your QUIZ grade:   ")
    laboratory_quiz_input, proceed = valid(laboratory_quiz_input)
    if proceed == 1:
        break

proceed = 0
while True:
    laboratory_assignment_input = input("Out of 100, please enter your ASSIGNMENT grade:   ")
    laboratory_assignment_input, proceed = valid(laboratory_assignment_input)
    if proceed == 1:
        break

proceed = 0
while True:
    laboratory_activities_input = input("Out of 100, please enter your ACTIVITY grade:   ")
    laboratory_activities_input, proceed = valid(laboratory_activities_input)
    if proceed == 1:
        break


proceed = 0
while True:
    laboratory_project_input = input("Out of 100, please enter your PROJECT grade:   ")
    laboratory_project_input, proceed = valid(laboratory_project_input)
    if proceed == 1:
        break

proceed = 0
while True:
    laboratory_recitation_input = input("Out of 100, please enter your RECITATION grade:   ")
    laboratory_recitation_input, proceed = valid(laboratory_recitation_input)
    if proceed == 1:
        break

proceed = 0
while True:
    laboratory_midterms_input = input("Out of 100, please enter your MIDTERMS grade:   ")
    laboratory_midterms_input, proceed = valid(laboratory_midterms_input)
    if proceed == 1:
        break

proceed = 0
while True:
    laboratory_finals_input = input("Out of 100, please enter your FINALS grade:   ")
    laboratory_finals_input, proceed = valid(laboratory_finals_input)
    if proceed == 1:
        break


#Computation part
#Initialize corresponding percentage
quiz_percentage = 25/100
assignment_activities_percentage = 15/100
project_percentage = 15/100
recitation_percentage = 10/100
midterms_finals_percentage = 35/100

#getting grade for lecture only
lecture_quiz_grade = float(lecture_quiz_input) * quiz_percentage
lecture_project_grade = float(lecture_project_input) * project_percentage
lecture_recitation_grade = float(lecture_recitation_input) * recitation_percentage

#special case for Assignment and Activities, and Midterms and Finals since they share a percentage
#Mean is solved for them and then multiplied to their corresponding percentage
#divided by 2 because there are 2 components that share the corresponding percentage
lecture_assignment_activity_mean = (float(lecture_assignment_input) + float(lecture_activities_input)) / 2
lecture_midterms_finals_mean = (float(lecture_midterms_input) + float(lecture_finals_input)) / 2

lecture_assignment_activity_grade = lecture_assignment_activity_mean * assignment_activities_percentage
lecture_midterms_finals_grade = lecture_midterms_finals_mean * midterms_finals_percentage

#getting grade for laboratory only
laboratory_quiz_grade = float(laboratory_quiz_input) * quiz_percentage
laboratory_project_grade = float(laboratory_project_input) * project_percentage
laboratory_recitation_grade = float(laboratory_recitation_input) * recitation_percentage

laboratory_assignment_activity_mean = (float(laboratory_assignment_input) + float(laboratory_activities_input)) / 2
laboratory_midterms_finals_mean = (float(laboratory_midterms_input) + float(laboratory_finals_input)) / 2

laboratory_assignment_activity_grade = laboratory_assignment_activity_mean * assignment_activities_percentage
laboratory_midterms_finals_grade = laboratory_midterms_finals_mean * midterms_finals_percentage

#Lecture grade
lecture_grade = lecture_quiz_grade + lecture_assignment_activity_grade + lecture_project_grade + lecture_recitation_grade + lecture_midterms_finals_grade

#Laboratory grade
laboratory_grade = laboratory_quiz_grade + laboratory_assignment_activity_grade + laboratory_project_grade + laboratory_recitation_grade + laboratory_midterms_finals_grade

#Initializing equivalent of laboratory and lecture to the final grade
lecture_percentage = 70/100
laboratory_percentage = 30/100

final_grade = (lecture_grade * lecture_percentage) + (laboratory_grade * laboratory_percentage)

#rounded up final grade to 2 decimal places
rounded_final_grade = round(final_grade,2)

print("\n")
name = name.upper()
#GPA conversion according to what was written on the board
if rounded_final_grade >= 96.5:
    print("Congratulations,",name+"!")
    print("Your GPA is, 1.00")
elif rounded_final_grade >= 93.5:
    print("Congratulations,",name+"!")
    print("Your GPA is, 1.25")
elif rounded_final_grade >= 90.5:
    print("Congratulations,",name+"!")
    print("Your GPA is, 1.50")
elif rounded_final_grade >= 87.5:
    print("Congratulations,",name+"!")
    print("Your GPA is, 1.75")
elif rounded_final_grade >= 84.5:
    print("Congratulations,",name+"!")
    print("Your GPA is, 2.00")
elif rounded_final_grade >= 81.5:
    print("Congratulations,",name+"!")
    print("Your GPA is, 2.25")
elif rounded_final_grade >= 78.5:
    print("Congratulations,",name+"!")
    print("Your GPA is, 2.50")
elif rounded_final_grade >= 75.5:
    print("Congratulations,",name+"!")
    print("Your GPA is, 2.75")
elif rounded_final_grade >= 74.5:
    print("Congratulations,",name+"!")
    print("Your GPA is, 3.00")
else:
    #displayed the grade to highlight the user of what grade they have that did not meet the 74.5 grade instead of just displaying "You Failed"
    print("Your GPA is 5.00, You unfortunately Failed,",name+".")