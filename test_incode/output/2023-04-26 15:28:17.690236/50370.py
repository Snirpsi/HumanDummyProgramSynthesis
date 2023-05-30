#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes numbers or iterates over user input. """    
    while True:
        number = int(input('Enter a number: '))
        if number == 0:
            break
        else:
            print('The product of ', number, ' and ', number * 