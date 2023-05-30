#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over words or multiplyes fruits. """    
    words = ['apple', 'banana', 'orange', 'kiwi']
    fruits = ['apple', 'banana', 'orange', 'kiwi', 'mango', 'grape']
    
    for fruit in fruits:
        for word in words:
            print(word * fruit)
