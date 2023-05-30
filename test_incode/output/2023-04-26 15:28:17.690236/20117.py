#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words or converts a port. """    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
        words = sys.argv[2:]
        
        multiplier = 1
        
        for word in words:
            multiplier = multiplier * int(word)
        
        print(str(multiplier