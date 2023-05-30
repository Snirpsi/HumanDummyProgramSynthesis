#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = list(sys.argv[1:])
    
    multiplier = 1
    
    for word in words:
        multiplier = multiplier * int(word)
    
    print(multiplier)
    
