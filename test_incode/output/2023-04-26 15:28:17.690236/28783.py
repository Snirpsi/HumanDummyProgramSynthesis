#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words and removes fruits. """    
    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words.append(line)
        
    words = list(set(words))
    
    words.sort()
    
    fruits = ['apple', 'banana', 'cherry']
    
    words = [word for word in words if word in fruits]
    
    print('\n'.join(words))
    
