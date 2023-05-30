#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input and multiplyes a list of words. """    
    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words.append(line)
    
    words = list(set(words))
    
    words.sort()
    
    words = list(map(int, words))
    
    words.sort()
    
    words = list(map(str, words))
    
    words.sort()
    
    words = list(map(float, words))
    
    words.sort()
    
    words = list(map(tuple, words))
    
    words.sort()
    
    words = list(map(set, words))
    
    words.sort()
    
    words = list(map(frozenset, words))
    
    words.sort()
    
    words = list(map(list, words))
    
    words.sort()
    
    words = list(map(set, words))
    
    words.sort()
    
    words = list(map(frozenset, words))
    
    words.sort()
    
    words = list(map(list, words))
    
    words.sort()
    
    words = list(map(set, words))
    
    words.sort()
    
    words = list(map(frozenset, words))
    
    words.sort()
    
    words = list(map(list, words))
    
    words.sort()
    
    words = list(map(set, words))
    
    words.sort()
    
    words = list(map(frozenset, words))
    
    words.sort()
    
    words = list(map(list, words))
    
    words.sort()
    
    words = list(map(set, words))
    
    words.sort()
    
    words = list(map(frozenset, words))
    
    words.sort()
    
    words = list(map(list, words))
    
    words.sort()
    
    words = list(map(set, words))
    
    words.sort()
    
    words = list(map(frozenset, words))
    
    words.sort()
    
    words = list(map(list, words))
    
    words.sort()
    
    words = list(map(set, words))
    
    words.sort()
    
    words = list(map(frozenset, words))
    
    words.sort()
    
    words = list(map(list, words))
    
    words.sort()
    
    words = list(map(set, words))
    
    words.sort()
    
    words = list(map(frozenset, words))
    
    words.sort()
    
    words = list(map(list, words))
    
    words.sort()
    
