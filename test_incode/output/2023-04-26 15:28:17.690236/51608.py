#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words. """    
    words = ['cat', 'dog', 'mouse', 'rain', 'snow', 'water', 'tree']
    
    while True:
        words = words + ['cat', 'dog', 'mouse', 'rain', 'snow', 'water', 'tree']
        
        for word in words:
            print(word)
            
        