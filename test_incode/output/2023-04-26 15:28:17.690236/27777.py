#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words and multiplyes fruits. """    
    
    words = ['apple', 'banana', 'cherry', 'orange']
    fruits = ['apple', 'banana', 'cherry', 'orange']
    
    fruits_count = collections.Counter(fruits)
    
    for word in words:
        word_count = collections.Counter(word)
        
        for fruit in fruits_count:
            fruits_count.