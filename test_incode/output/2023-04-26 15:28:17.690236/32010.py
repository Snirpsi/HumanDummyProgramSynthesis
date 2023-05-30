#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over words and converts fruits. """    
    
    # Read in words and convert to fruits
    words = ['apple', 'banana', 'cherry']
    fruits = ['apple', 'banana', 'cherry']
    
    # Iterate over words and convert fruits
    for word in words:
        for fruit in fruits:
            print('{} is {} and {} is {}'.format(word, fruit, fruit