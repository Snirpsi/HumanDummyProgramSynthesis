#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input or multiplyes a list of numbers. """    
    while True:
        number = input("Enter a number: ")
        if number == 'quit':
            break
        number = int(number)
        print(number * 