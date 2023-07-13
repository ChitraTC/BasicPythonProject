# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y

# This function finds modulus of two numbers
def modulus(x, y):
    return x % y

# This function Exponential of two numbers
def Exponen(x, y):
    return x ** y

# This function floor divides two numbers
def fdivide(x, y):
    return x // y

# This function floor divides two numbers
def fdivide(x, y):
    return x // y






while True:
    # take input from the user
    choice = input("Enter Operation(+/-/*///%/**///): ")


    if choice in ('+', '-', '*', '/','%','**','//'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '+':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '/':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '%':
            print(num1, "%", num2, "=", modulud(num1, num2))

        elif choice == '**':
            print(num1, "**", num2, "=", Exponen(num1, num2))

        elif choice == '//':
            print(num1, "//", num2, "=", fdivide(num1, num2))

            break
    else:
        print("Invalid Input")
