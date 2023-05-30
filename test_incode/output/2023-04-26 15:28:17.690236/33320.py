#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over fruits or adds all ports. """    
    while True:
        fruit = input('Enter a fruit or type "quit" to quit.')
        if fruit == 'quit':
            break
        else:
            print('You entered', fruit)
            print('Adding ports...')
            ports = input('Enter a port or type "quit" to quit.')
            if ports == 'quit':
                break
            else:
                print('You entered', ports)
                