#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers or prints a list of numbers. """    
    while True:
        try:
            line = input('Enter a number: ')
            line = float(line)
            if line > 0:
                print('The number you entered is ' + str(line))
            else:
                print('The number you entered is ' + str(line) + ' 