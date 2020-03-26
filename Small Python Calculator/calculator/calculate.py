from operations import *
class Calculate():
    def calculate():
        operation_choice = ''
        print("After entering 2 numbers, you will be prompted to enter an operation.")
        while operation_choice != 'quit':
            while True:
                try:
                    num1 = int(input("Enter first number: "))
                except ValueError:
                    print("That's not a number. Please enter a number: ")
                    continue
                else:
                    break
            while True:
                try:
                    num2 = int(input("Enter second number: "))
                except ValueError:
                    print("That's not a number. Please enter a number: ")
                    continue
                else:
                    break
            print()
            print("1 Add")
            print("2 Subtract")
            print("3 Multiply")
            print("4 Divide")
            print("'Quit' to close")
            print()
            while True:
                try:
                    operation_choice = input("Enter an operation: ")
                except ValueError:
                    print("That was not a valid choice.")
                    continue
                else:
                    break
            if operation_choice == '1':
                print(Operations.add(num1,num2))
            elif operation_choice == '2':
                print(Operations.subtract(num1, num2))
            elif operation_choice == '3':
                print(Operations.multiply(num1, num2))
            elif operation_choice == '4':
                error_message = 'ERROR: Cannot divide by 0'
                print(Operations.divide(num1, num2, error_message))
            elif operation_choice == 'Quit':
                print("Exiting calculator")
                break;
            else:
                print("Please enter an operation choice.")
            print()
    calculate()
