#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers or stores words. """    
    while True:
        line = input('Enter a number: ')
        try:
            number = int(line)
        except ValueError:
            print('That is not a number')
        else:
            if number > 0:
                print(number)
            else:
                print('That is not a number')
