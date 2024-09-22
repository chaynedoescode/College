# Exercise 2: Ohm’s Law Calculator

try:
    # 1.Ask the user what they want to calculate: Voltage, Current, or Resistance.
    print("[1] Voltage")
    print("[2] Current")
    print("[3] Resistance")
    find_variable = int(input("Enter corresponding number to find: "))

    if find_variable == 1:
        # 2.Based on their choice, prompt the user to input the appropriate values.
        current = float(input("Enter current value: "))
        resistance = float(input("Enter resistance value: "))
        # 3.Use Ohm's Law to calculate the missing variable and display the result.
        voltage = current * resistance
        print(voltage)

    elif find_variable == 2:
        voltage = float(input("Enter voltage value: "))
        resistance = float(input("Enter resistance value: "))
        current = voltage / resistance
        print(current)

    elif find_variable == 3:
        voltage = float(input("Enter voltage value: "))
        current = float(input("Enter current value: "))
        resistance = voltage / current
        print(resistance)
        
    else:
        print("Enter only 1,2, or 3")

except ValueError:
    print("Invalid Input!")

# 4.Handle cases where division by zero might occur.
except ZeroDivisionError:
    print("Can not divide by Zero!")
