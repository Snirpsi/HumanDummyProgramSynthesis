#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words and enumerates fruits. """    
    
    words = ['apple', 'banana', 'cherry']
    fruits = ['apple', 'banana', 'cherry']
    
    for word in words:
        for fruit in fruits:
            print(word, fruit)
            
