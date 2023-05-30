#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits and multiplyes a list of words. """    
    fruits = ['apple', 'banana', 'cherry']
    words = ['apples', 'bananas', 'cherries']
    
    for fruit in fruits:
        for word in words:
            print(