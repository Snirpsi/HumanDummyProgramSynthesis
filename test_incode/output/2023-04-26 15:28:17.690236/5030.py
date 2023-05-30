#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits and iterates over a port. """    
    
    port = int(sys.argv[1])
    
    fruits = ['apple', 'banana', 'cherry']
    
    for fruit in fruits:
        print('{} is {} 