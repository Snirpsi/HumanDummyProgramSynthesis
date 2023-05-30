#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input or iterates over numbers. """    
    while True:
        number = int(input('Enter a number: '))
        if number < 0 or number > 100: 
            print('Invalid input. Try again.')
        else:
            print('You entered', number)
            break
    print('Goodbye!')
