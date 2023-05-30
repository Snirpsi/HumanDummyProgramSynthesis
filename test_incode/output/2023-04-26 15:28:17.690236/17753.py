#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints numbers or opens words. """    
    while True:
        number = input('Enter a number: ')
        if number == 'quit':
            break
        else:
            print(number)
