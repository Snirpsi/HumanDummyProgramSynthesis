#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a list of words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['cat', 'dog', 'mouse']
    
    words = list(set(words))
    
    words.sort()
    
    for word in words:
        print(word)
    
