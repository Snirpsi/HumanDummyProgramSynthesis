#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers or multiplyes a port. """    
    while True:
        number = input("Enter a number: ")
        if number == 'quit':
            break
        elif number.isdigit():
            number = int(number)
            print(number * 