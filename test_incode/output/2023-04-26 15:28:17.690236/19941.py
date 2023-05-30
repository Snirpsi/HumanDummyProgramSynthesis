#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words. """    
    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if not line:
            continue
        
        words = line.split(' ')
        
        for word in words:
            word = word.strip()
            
            if word:
                words.remove(word)
    
    print(' '.join(words))
    
    