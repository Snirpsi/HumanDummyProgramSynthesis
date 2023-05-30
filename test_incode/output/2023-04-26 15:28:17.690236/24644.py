#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input. """    
    while True:
        line = input('Enter a number: ')
        try:
            number = int(line)
            break
        except ValueError:
            print('That is not a number')
            
    print('You entered', number, '