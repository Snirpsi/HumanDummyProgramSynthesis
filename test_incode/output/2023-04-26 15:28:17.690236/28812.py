#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words. """    
    words = ['cat', 'dog', 'mouse', 'bird', 'cat', 'dog', 'mouse', 'bird', 'cat', 'dog', 'mouse', 'bird']
    
    i = 0
    while i < len(words):
        print(words[i])
        i += 1
        
