#Frenzen Code
def calculate_sum(num1, num2):
    
    return num1 + num2


def main():
    print("This is a simple adder program.\n")

    try:
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))

        result = calculate_sum(first_number, second_number)
        print("The sum is:", result)

    except ValueError:
        print("Invalid input! Please enter valid numbers.")
    except Exception as error:
        print("An unexpected error occurred:", error)


if __name__ == "__main__":
    main()