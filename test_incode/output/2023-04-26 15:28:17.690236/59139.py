#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input. """    
    while True:
        answer = input('Enter a number: ')
        try:
            answer = int(answer)
        except ValueError:
            print('That is not a valid number')
        else:
            print('You entered a number:', answer)
