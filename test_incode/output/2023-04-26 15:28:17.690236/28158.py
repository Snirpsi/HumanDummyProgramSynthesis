#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input and multiplyes a list of words. """    
    import sys
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        words.append(line)
    
    words = list(set(words))
    
    words.sort()
    
    multiplier = 1
    
    for word in words:
        multiplier = multiplier * int(word)
    
    print(multiplier)
    
    