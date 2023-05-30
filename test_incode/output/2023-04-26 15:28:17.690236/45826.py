#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words. """    
    import sys
    
    words = []
    for line in sys.stdin:
        words.append(line.strip())
    
    words.sort()
    
    multiplied = []
    for word in words:
        multiplied.append(word[0] * word[1])
    
    print(' '.join(map(str, multiplied)))
    
