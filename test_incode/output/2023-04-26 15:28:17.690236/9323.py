#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers or opens user input. """    
    while True:
        number = int(input('Enter a number: '))
        if number == -1:
            print('Bye!')
            break
        else:
            print(number)
