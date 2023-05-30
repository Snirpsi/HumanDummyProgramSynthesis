#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words or adds a list of words. """    
    import sys
    
    words = []
    for arg in sys.argv[1:]:
        words.append(arg)
    
    if len(words) == 0:
        print("Usage: %s <words>" % sys.argv[0])
        exit(1)
    
    words = list(set(words))
    
    multiplier = 1
    for word in words:
        multiplier = multiplier * int(word)
    
    print(multiplier)
    
