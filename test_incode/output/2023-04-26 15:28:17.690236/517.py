#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = []
    
    for word in words:
        word = word.strip()
        
        if word == '':
            continue
        
        if word in 