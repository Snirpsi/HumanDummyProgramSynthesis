#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words. """    
    words = ['cat', 'dog', 'mouse', 'chicken', 'horse', 'monkey', 'bird']
    
    while True:
        for word in words:
            print(word)
        
        print('\nPress a key to exit.')
        
        input()
        
