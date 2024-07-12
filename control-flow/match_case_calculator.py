num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

operation = input("Choose the operation (+, -, *, /):")

match operation:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2  
    case '/':
        if num2 == 0:
            print("cannot divide by zero.") 
        else:
            result = num1 / num2
    case _:
        print("Invalid operation. Please choose from '+', '-', '*', '/'.")


if operation in ['+', '_', '*']:
    print(f"The result of {num1} {operation} {num2} is {result}.")
elif operation == '/' :
    if num2 != 0:
        print(f"The result of {num1} {operation} {num2} is {result}.") 
else:
    print("operation not supported or invalid output.")

              