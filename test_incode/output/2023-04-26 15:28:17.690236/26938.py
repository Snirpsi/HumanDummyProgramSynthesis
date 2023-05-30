#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits or iterates over a port. """    
    port = '/dev/ttyUSB0'
    
    while True:
        fruit = input('Enter a fruit: ')
        if fruit == 'exit':
            break
        else:
            print('Fruit is', fruit)
            
    
