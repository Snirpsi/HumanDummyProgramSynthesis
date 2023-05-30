#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers or stores user input. """    
    while True:
        number = input("Enter a number: ")
        if number.isdigit():
            number = int(number)
            print(number)
        else:
            print("Invalid input. Try again.")
