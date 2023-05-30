#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a list of words or calculates a list of words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = [word.strip() for word in sys.argv[1].split(',')]
    else:
        words = []
    
    words.extend(sys.argv[2:])
    
    words = list(set(words))
    
    words.sort()
    
    for word in words:
        print(word)
    
