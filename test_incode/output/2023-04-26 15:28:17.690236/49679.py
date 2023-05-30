#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates user input or iterates over fruits. """    
    while True:
        print("Welcome to the Fruit Calculator!")
        print("Please select one of the following options")
        print("1. Add two numbers")
        print("2. Subtract two numbers")
        print("3. Multiply two numbers")
        print("4. Divide two numbers")
        print("5. Quit")
        choice = input("Please select an option: ")
        if choice == "1":
            print("Please enter the first number: ")
            first_num = input("Please enter the first number: ")
            print("Please enter the second number: ")
            second_num = input("Please enter the second number: ")
            answer = first_num + second_num
            print("The answer is", answer)
        elif choice == "2":
            print("Please enter the first number: ")
            first_num = input("Please enter the first number: ")
            print("Please enter the second number: ")
            second_num = input("Please enter the second number: ")
            answer = first_num - second_num
            print("The answer is", answer)
        elif choice == "3":
            print("Please enter the first number: ")
            first_num = input("Please enter the first number: ")
            print("Please enter the second number: ")
            second_num = input("Please enter the second number: ")
            answer = first_num * second_num
            print("The answer is", answer)
        elif choice == "4":
            print("Please enter the first number: ")
            first_num = input("Please enter the first number: ")
            print("Please enter the second number: ")
            second_num = input("Please enter the second number: ")
            answer = first_num / second_num
            print("The answer is", answer)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
