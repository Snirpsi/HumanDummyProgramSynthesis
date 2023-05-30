#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words and removes fruits. """    
    
    words = ['apple', 'banana', 'cherry', 'orange', 'pear']
    
    for word in words:
        print(word)
        
    fruits = ['apple', 'banana', 'cherry', 'orange', 'pear']
    
    for fruit in fruits:
        if fruit not in words:
            print(