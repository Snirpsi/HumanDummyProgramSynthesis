#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that requests user input.
    while True:
        print("Enter a number: ")
        number = int(input())
        if number > 100 or number < 1:
            print("Invalid input. Please try again.")
        else:
            break
    #A loop that prints out the number the user entered.
    while True:
        print(number)
        number = int(input())
        if number > 100 or number < 1:
            print("Invalid input. Please try again.")
        else:
            break

