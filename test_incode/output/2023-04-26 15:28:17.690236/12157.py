#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits and iterates over a list of words. """    
    fruits = ['apple', 'banana', 'cherry']
    
    words = ['apple', 'banana', 'cherry']
    
    while True:
        fruits.append(fruits.pop(0))
        words.append(words.pop(0))
        
        print(fruits)
        print(words)
        
        if fruits:
            print(