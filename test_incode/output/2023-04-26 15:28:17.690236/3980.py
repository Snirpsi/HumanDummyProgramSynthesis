#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        print('Current fruit:', fruits)
        fruits = input('Enter a fruit: ')
        if fruits == 'q':
            break
        else:
            print('Invalid input. Try again.')
