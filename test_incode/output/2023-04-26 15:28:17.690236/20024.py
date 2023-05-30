#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words and multiplyes a list of words. """    
    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if not line:
            continue
        
        words = line.split(' ')
        
        for word in words:
            word = word.strip()
            
            if not word:
                continue
            
            words.append(word)
            
    words.sort()
    
    for word in words:
        print(word