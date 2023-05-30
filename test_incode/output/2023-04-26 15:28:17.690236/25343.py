#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words and removes fruits. """    
    
    import sys
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        
        if line:
            words.append(line)
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word not in ['apple', 'banana', 'cherry']]
    
    print('\n'.join(words))
    
