#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that opens a list of numbers.
    #The user can then choose to quit or continue to input numbers.
    while True:
        choice = input("Enter a number: ")
        if choice == 'q':
            break
        elif choice in numbers:
            print(choice)
        else:
            print("Invalid input")

