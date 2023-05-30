#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over fruits. """    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    while True:
        for fruit in fruits:
            print('The fruit is', fruit)
        time.sleep(5)
