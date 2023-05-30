#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers or prints numbers. """    
    while True:
        try:
            number = int(input('Enter a number: '))
            if number > 0 and number < 10:
                print(number)
            else:
                print('Invalid number')
        except ValueError:
            print('Invalid number')
