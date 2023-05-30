#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits and iterates over a list of words. """    
    
    words = ['apple', 'banana', 'cherry']
    
    # Remove fruits from words and iterate over them
    fruits = ['apple', 'banana', 'cherry']
    
    for fruit in fruits:
        if fruit in words:
            words.remove(fruit)
    
    for word in words:
        print(word)
        
