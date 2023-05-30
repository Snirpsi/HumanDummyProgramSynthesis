#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints numbers or returns user input. """    
    while True:
        number = input('Enter a number: ')
        if number == 'q':
            break
        else:
            print(number)
