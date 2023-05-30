#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port or adds fruits. """    
    while True:
        fruit = input('Enter a fruit: ')
        if fruit == 'quit':
            print('Goodbye!')
            break
        else:
            print('You entered ' + fruit)
            port = int(input('Enter a port: '))
            fruit = fruit + ' ' + 