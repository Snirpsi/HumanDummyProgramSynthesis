#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words or prints fruits. """    
    
    words = ['apple', 'banana', 'cherry']
    
    while True:
        fruits = []
        
        for word in words:
            if word in words:
                fruits.append(word)
        
        print('\n'.join(