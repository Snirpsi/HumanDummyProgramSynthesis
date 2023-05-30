#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input or prints a list of numbers. """    
    while True:
        number = input("Enter a number: ")
        if number == "":
            break
        else:
            print(number)
