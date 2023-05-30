#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words. """    
    words = ['cat', 'dog', 'mouse', 'bird', 'cat', 'dog', 'mouse', 'bird', 'cat', 'dog', 'mouse', 'bird']
    
    words.sort()
    
    for word in words:
        print(word)
        
