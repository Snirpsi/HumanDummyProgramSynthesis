#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores user input or calculates numbers. """    
    while True:
        number = input("Enter a number: ")
        if number.isdigit():
            number = int(number)
            print(number)
        else:
            print("Invalid input")
            break
