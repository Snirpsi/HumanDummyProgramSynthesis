#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input or enumerates a list of numbers. """    
    while True:
        number = input("Enter a number: ")
        if number == '':
            break
        else:
            print(number)

<|/ file filename=