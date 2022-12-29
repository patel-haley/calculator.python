# Calculate simple 2 number operations

print("Select an operation to perform:")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()

if operation == "1":
    #code for addition
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print(num1 + "+" + num2 + "=" + str(int(num1) + int(num2)))
elif operation == "2":
    #code for subtraction
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print(num1 + "-" + num2 + "=" + str(int(num1) - int(num2)))
elif operation == "3":
    #code for multiplication
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print(num1 + "x" + num2 + "=" + str(int(num1) * int(num2)))
elif operation == "4":
    #code for division
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print(num1 + "/" + num2 + "=" + str(int(num1) / int(num2)))
else:
    print("Invalid Input")


