# Exercise 1: Temperature Converter
# Create a program that converts temperatures between Celsius and Fahrenheit.

try:
    # 1.	Ask the user to input a temperature.
    temperature = float(input("Enter temperature: "))
    print("[1] Celsius to Fahrenheit ")
    print("[2] Fahrenheit to Celsius")
    # 2.	Ask the user to select the conversion type: from Celsius to Fahrenheit or from Fahrenheit to Celsius.
    conversion = int(input("Enter conversion 1 or 2: "))

    # 3.	Perform the appropriate conversion and print the result.
    if conversion == 1:
        converted = (temperature * 9/5) + 32
        print(converted)
    elif conversion == 2:
        converted = (temperature -32) * 5/9
        print(converted)
    else:
        raise ValueError

# Handle invalid input (non-numeric temperature or invalid conversion option)
except ValueError:
    print("Invalid Input")
