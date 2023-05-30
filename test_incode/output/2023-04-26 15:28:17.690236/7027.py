#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of numbers or removes user input. """    
    while True:
        try:
            number = int(input('Enter a number: '))
            if number == -1:
                break
            print(number)
        except ValueError:
            print('Invalid input')
