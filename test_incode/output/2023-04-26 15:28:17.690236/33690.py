#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words. """    
    import sys
    words = [line.strip() for line in sys.stdin]
    
    total = 0
    for word in words:
        total += word
        
    print(total)
    
