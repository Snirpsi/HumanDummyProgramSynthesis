#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port or iterates over fruits. """    
    
    port = int(sys.argv[1])
    
    if port == 8080:
        fruits = ['apple', 'orange', 'banana', 'cherry']
    else:
        fruits = ['apple', 'orange', 'banana', 'cherry']
    
    for fruit in fruits:
        print('{} is {}!'.format(fruit, 