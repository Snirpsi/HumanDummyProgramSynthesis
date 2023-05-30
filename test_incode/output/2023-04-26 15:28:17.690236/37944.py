#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words or opens fruits. """    
    while True:
        fruits = input('Enter a fruit: ')
        if fruits == 'exit':
            break
        else:
            print(