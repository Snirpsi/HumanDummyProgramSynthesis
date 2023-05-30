#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints numbers or multiplyes user input. """    
    while True:
        number = int(input('Enter a number: '))
        if number == 0:
            break
        else:
            print(number * 2)
