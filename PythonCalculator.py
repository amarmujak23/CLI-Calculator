import time
import sys

#curretnly no dvisiion by zero handling, will add in future update

print("Welcome!")

selection = {
    "1": "Addition (+)",
    "2": "Subtraction (-)",
    "3": "Multiplication (x)",
    "4": "Division (/)",
    "5": "Modulus (%)",
    "6": "Exponent (**)",
    "7": "Exit",
}

# Ask user if they want to repeat
def repeat_calc(operation_name):
    while True:
        time.sleep(1.2)
        choice = input(
            f"Would you like to perform another {operation_name} problem? (y/n): "
        ).strip().lower()

        if choice in ("y", "n"):
            return choice
        print("Invalid input. Please type y or n.")

# Generic math operation runner
def run_operation(operation_name, func):
    while True:
        try:
            num1 = int(input("Enter first integer: "))
            num2 = int(input("Enter second integer: "))
            result = func(num1, num2)
            print(f"The answer to {num1} {operation_name} {num2} = {result}")

            repeat = repeat_calc(operation_name)
            if repeat == "y":
                print("...")
                time.sleep(1.8)
                continue
            else:
                print("Returning to main menu...")
                time.sleep(2)
                break

        except ValueError:
            print("Invalid Input, please enter integers only")
            continue

        

# Individual math operations
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b
def mod(a, b): return a % b
def exp(a, b): return a ** b

# Map menu options to operations
operations = {
    "1": ("+", add),
    "2": ("-", sub),
    "3": ("x", mul),
    "4": ("/", div),
    "5": ("%", mod),
    "6": ("**", exp),
}

# Main menu loop
while True:
    for key, value in selection.items():
        print(f"Option {key}: {value}")

    user_input = input("Please select math operator: ").strip()

    if user_input in operations:
        symbol, func = operations[user_input]
        time.sleep(1.5)
        print(f"You have chosen Option {user_input}: {selection[user_input]}")
        run_operation(symbol, func)
        continue

    if user_input == "7":
        print("Exiting Calculator...")
        time.sleep(2)
        print("Goodbye")
        sys.exit()

    print("Incorrect Format, please select a valid option from the menu.")
    time.sleep(2)