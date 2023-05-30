#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits or removes all ports. """    
    while True:
        fruit = input('Enter a fruit: ')
        if fruit == '':
            break
        else:
            print('Fruit ' + fruit + ' is ' + 