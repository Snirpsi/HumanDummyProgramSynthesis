#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        print('Current fruits:', fruits)
        fruits = input('Enter a fruit: ')
        if fruits == 'exit':
            break
        else:
            print('You entered', fruits)
            