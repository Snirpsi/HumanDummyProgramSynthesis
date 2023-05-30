#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates numbers or multiplyes a list of numbers. """    
    while True:
        number = input('Enter a number: ')
        if number == 'quit':
            break
        else:
            print(number * 2)
            print('\n')
    print('Thank you for using the 