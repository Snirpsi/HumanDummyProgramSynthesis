#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers or opens a list of numbers. """    
    while True:
        number = input("Enter a number: ")
        if number == "q":
            break
        elif number.isdigit():
            print(number)
        else:
            print("Invalid input. Try again.")
