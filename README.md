# Python Calculator

A simple command-line calculator that performs basic arithmetic operations with an interactive menu interface.

## Features

- **Addition (+)** - Add two integers
- **Subtraction (-)** - Subtract two integers
- **Multiplication (x)** - Multiply two integers
- **Division (/)** - Divide two integers
- **Modulus (%)** - Get remainder of division
- **Exponent (**)** - Raise a number to a power
- **Repeat Option** - Perform multiple calculations without restarting
- **Input Validation** - Ensures only integers are entered

## Usage

Run the calculator:

```bash
python PythonCalculator.py
```

1. The program displays a menu with operation options (1-7)
2. Enter the number of your desired operation
3. Enter two integers when prompted
4. View the result
5. Choose to perform another calculation or return to the main menu
6. Select option 7 to exit

## Example

```
Welcome!
Option 1: Addition (+)
Option 2: Subtraction (-)
Option 3: Multiplication (x)
Option 4: Division (/)
Option 5: Modulus (%)
Option 6: Exponent (**)
Option 7: Exit
Please select math operator: 1
You have chosen Option 1: Addition (+)
Enter first integer: 5
Enter second integer: 3
The answer to 5 + 3 = 8
Would you like to perform another + problem? (y/n): n
Returning to main menu...
```

## Known Limitations

- Only accepts integer input
- Division by zero is not currently handled (planned for future update)

## Requirements

- Python 3.x

## Future Improvements

- Add division by zero handling
- Support for floating-point numbers
- Additional operations (square root, factorial, etc.)
