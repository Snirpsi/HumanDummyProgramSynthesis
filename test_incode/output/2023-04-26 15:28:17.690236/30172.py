#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers and removes user input. """    
    while True:
        try:
            number = int(input('Enter a number: '))
            if number > 0:
                print('The number you entered is', number)
            else:
                print('The number you entered is', number, '