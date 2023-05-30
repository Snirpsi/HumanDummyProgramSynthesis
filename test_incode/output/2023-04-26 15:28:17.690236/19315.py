#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits and iterates over a list of words. """    
    fruits = ['apple', 'banana', 'cherry']
    words = ['apple', 'banana', 'cherry']
    
    # Create a loop that multiplies fruits and iterates over a list of words.
    for fruit in fruits:
        for word in words:
            print(word * fruit)
            
