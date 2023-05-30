#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words. """    
    
    import sys
    
    words = []
    
    for word in sys.stdin:
        words.append(word.strip())
        
    words = list(set(words))
    
    words.sort()
    
    sys.stdout.write(" ".join(words))
    
