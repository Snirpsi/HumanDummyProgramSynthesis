#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of words. """    
    
    import sys
    
    words = [sys.argv[1], sys.argv[2], sys.argv[3]]
    
    multiplied = []
    
    for word in words:
        multiplied.append(word*int(sys.argv[4]))
    
    print(" ".join(multiplied))
    
