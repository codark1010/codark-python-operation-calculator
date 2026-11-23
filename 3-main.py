left = float(input("First number: "))
operation = input("Operation: ")
right = float(input("Second number: "))
if operation == "+": print(left + right)
elif operation == "-": print(left - right)
elif operation == "*": print(left * right)
elif operation == "/":
    if right == 0:
        print("Cannot divide by zero")
    else:
        print(left / right)
else: print("Unsupported operation")
