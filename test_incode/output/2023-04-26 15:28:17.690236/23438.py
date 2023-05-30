#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words or iterates over a port. """    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    for word in sys.argv[2:]:
        words.append(word)
    
    words = list(set(words))
    
    multiplier = 1
    
    for word in words:
        multiplier = multiplier * int(word)
    
    print(multiplier)
    
