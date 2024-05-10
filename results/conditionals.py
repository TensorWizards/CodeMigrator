# Identification Division
program_name = "CONDITIONALS"

# Data Division
# Working-Storage Section
num1 = 10
num2 = 5
num3 = 15
num4 = 20
check_val = 75

# Procedure Division
# Main Logic
if num1 > num2:
    if num3 > num4:
        print("NUM1 is greater than NUM2 and NUM3 is greater than NUM4.")
    else:
        print("NUM1 is greater than NUM2 but NUM3 is not greater than NUM4.")
else:
    print("NUM1 is not greater than NUM2.")

# Custom Predefined Conditions
if check_val >= 41 and check_val <= 100:
    print("CHECK-VAL passed the test.")
elif check_val >= 0 and check_val <= 40:
    print("CHECK-VAL failed the test.")
else:
    print("CHECK-VAL is out of range.")

# SWITCH Statement
true = True
if num1 < 2:
    print("NUM1 is less than 2.")
elif num1 < 19:
    print("NUM1 is less than 19.")
elif num1 < 1000:
    print("NUM1 is less than 1000.")
else:
    print("NUM1 is greater than or equal to 1000.")

# STOP RUN Statement
print("Program execution ended.")