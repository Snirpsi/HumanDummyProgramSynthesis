#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input and iterates over numbers. """    
    while True:
        number = input("Enter a number: ")
        if number == "":
            break
        else:
            print(number)
