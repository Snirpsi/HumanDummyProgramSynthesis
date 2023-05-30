#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words and multiplyes fruits. """    
    words = ['apple', 'banana', 'cherry']
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        fruits = fruits * len(words)
        
        for word in words:
            print(word + ' ' + fruits)
        
        words = ['apple', 'banana', 'cherry']
        
