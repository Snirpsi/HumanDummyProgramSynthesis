#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over fruits and multiplyes a list of words. """    
    fruits = ['apple', 'orange', 'banana', 'pear', 'kiwi']
    words = ['apple', 'orange', 'banana', 'pear', 'kiwi']
    
    for fruit in fruits:
        for word in words:
            print(word*fruit)
    
