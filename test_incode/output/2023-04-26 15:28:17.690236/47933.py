#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores numbers. """    
    while True:
        number = int(input('Enter a number: '))
        if number == 999:
            print('You entered a number that equals 999.')
            break
        else:
            print('You entered a number that does not equal 999.')
            