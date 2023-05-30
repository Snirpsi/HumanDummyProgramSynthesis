#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints fruits and enumerates words. """    
    
    fruits = ['apple', 'banana', 'cherry']
    words = enumerate(fruits)
    
    for word, count in words:
        print('{}: {}'.format(word, count))
        
