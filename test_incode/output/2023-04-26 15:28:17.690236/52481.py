#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens numbers. """    
    while True:
        number = int(input('Enter a number: '))
        if number < 10:
            print('The number you entered is too small')
        elif number > 1000:
            print('The number you entered is too large')
        else:
            print('The number you entered is correct')
            break
    print('Thank you for using my program!')
