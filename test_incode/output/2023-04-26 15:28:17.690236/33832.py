#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints fruits. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    while True:
        print('\n'.join(fruits))
        time.sleep(1)
