import math

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):

    if y == 0:
        return "Error: Division by zero!"

    else:
        return x / y

def square_root(x):

    if x < 0:
        return "Error: Square root of a negative number!"

    else:
        return math.sqrt(x)


def power(x, y):
    return x ** y


def sin(x):
    return math.sin(math.radians(x))


def cos(x):
    return math.cos(math.radians(x))


def tan(x):
    return math.tan(math.radians(x))


def scientific_calculator():
    print("Welcome to the Scientific Calculator!")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Power")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Exit")


    while True:
        choice = input("Enter your choice (1-10): ")


        if choice in ['1', '2', '3', '4', '6']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))

            elif choice == '2':
                print("Result:", subtract(num1, num2))

            elif choice == '3':
                print("Result:", multiply(num1, num2))

            elif choice == '4':
                print("Result:", divide(num1, num2))

            elif choice == '6':
                print("Result:", power(num1, num2))

        elif choice in ['5']:
            num = float(input("Enter a number: "))
            if choice == '5':
                print("Result:", square_root(num))
        elif choice in ['7', '8', '9']:
            angle = float(input("Enter the angle in degrees: "))
            if choice == '7':
                print("Result:", sin(angle))
            elif choice == '8':
                print("Result:", cos(angle))
            elif choice == '9':
                print("Result:", tan(angle))

        elif choice == '10':
            print("Thank you for using the Scientific Calculator!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    scientific_calculator()



