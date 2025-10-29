# First fixed-version, specified by team.

# Summation of two numbers.
def calculateSum(firstNumber, secondNumber):
  return firstNumber + secondNumber


# Main Program
def main( ):
  print("This is a simple adder program. \n")

  try:
    firstNumber = float(input("Enter first number: "))
    secondNumber = float(input("Enter second number: "))

    sum = calculateSum(firstNumber, secondNumber)

    print("\n The sum is :", sum)

  except ValueError:
    print("Value Error: Please input a valid number.")


# Call the function at end.
main() 


# Vien Code Accepted, Second fixed-version accepted
"""
This program prompts the user for two numbers, calculates their sum,
and prints the result. It attempts input conversion once and handles
errors by exiting on failure.
"""

def addNumbers(numOne, numTwo):
    return numOne + numTwo


def runSimpleAdder():
    print("This is a simple adder program\n")

    try:
        firstNumberStr = input("Enter the first number: ")
        secondNumberStr = input("Enter the second number: ")

        firstNumber = int(firstNumberStr)
        secondNumber = int(secondNumberStr)
        
        totalSum = addNumbers(firstNumber, secondNumber)

        print(f"The sum is: {totalSum}")
        
    except ValueError:
        print("Invalid input. Please enter only whole numbers. Exiting program.")

runSimpleAdder()

# Two versions are accepted, select one of the source code.
