#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words and multiplyes words. """    
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if not line:
            continue
        
        words.append(line)
        
    words.sort()
    
    for word in words:
        
        words = word.split()
        
        words = [str(word) for word in words]
        
        words = [word * int(i) for i in words]
        
        print(' '.join(words))
        
