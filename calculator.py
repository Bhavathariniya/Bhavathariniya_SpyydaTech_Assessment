history = []

def add(a, b):
    result = a + b
    history.append(f"{a} + {b} = {result}")
    return result


def subtract(a, b):
    result = a - b
    history.append(f"{a} - {b} = {result}")
    return result


def multiply(a, b):
    result = a * b
    history.append(f"{a} * {b} = {result}")
    return result


def divide(a, b):
    if b == 0:
        history.append(f"{a} / {b} = Error")
        return "Error (Division by zero)"

    result = a / b
    history.append(f"{a} / {b} = {result}")
    return result


def get_history():
    return history

print("Calculator\n")

while True:
    print("Select operations: +  -  *  /")
    print("or")
    print("2 . history")
    print("3 .quit")

    choice = input("Your choice: ").strip()

    if choice == "3":
        print("Exiting")
        break

    if choice == "2":
        print("\n History: ")
        for item in get_history():
            print(item)
        print()
        continue

    if choice in ["+", "-", "*", "/"]:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Enter valid numbers.\n")
            continue

        if choice == "+":
            print("Result:", add(a, b))
        elif choice == "-":
            print("Result:", subtract(a, b))
        elif choice == "*":
            print("Result:", multiply(a, b))
        elif choice == "/":
            print("Result:", divide(a, b))

        print() 

    else:
        print("Invalid option\n")
