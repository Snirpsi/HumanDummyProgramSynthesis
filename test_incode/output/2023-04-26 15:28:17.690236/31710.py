#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates fruits or converts a port. """    
    
    fruit = sys.argv[1]
    
    if fruit == 'fruit':
        fruits = ['apple', 'banana', 'cherry']
    elif fruit == 'fruits':
        fruits = ['apple', 'banana', 'cherry']
    else:
        print('Usage: %s fruit' % sys.argv[0])
        exit(1)
    
    for fruit in fruits:
        print('%s -> %s' % (fruit, 