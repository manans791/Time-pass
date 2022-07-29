"""num1=float(input("Enter your first number: "))
num2=float(input("Enter your second number: "))
operator=input("Enter the operator: ")"""


def calculator(num1, num2, operator):
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
    else:
        print("Invalid Operator")


calculator(1000, 100, "/")
