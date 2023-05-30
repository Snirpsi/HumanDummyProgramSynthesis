#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words and returns fruits. """    
    
    import sys
    
    words = []
    fruits = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words.append(line)
        
        if line == 'apple':
            fruits.append('apple')
        elif line == 'orange':
            fruits.append('orange')
        elif line == 'banana':
            fruits.append('banana')
        elif line == 'cherry':
            fruits.append('cherry')
        else:
            fruits.append('unknown')
    
    print('\n'.join(words))
    print('\n'.join(fruits))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
