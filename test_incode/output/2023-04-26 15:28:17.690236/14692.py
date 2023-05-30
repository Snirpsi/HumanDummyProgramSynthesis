#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of numbers or stores user input. """    
    while True:
        num = input('Enter a number: ')
        if num == 'q':
            break
        else:
            print(num)
            