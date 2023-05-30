#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints fruits or adds numbers. """    
    while True:
        print('Type a fruit or press enter to add numbers')
        fruit = input('> ')
        if fruit == '':
            break
        else:
            print(