#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        print('\n'.join(fruits))
        time.sleep(1)
        
