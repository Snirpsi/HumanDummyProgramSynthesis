#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words and removes a port. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 remove-port.py <words>")
        sys.exit()
    
    words = sys.argv[1:]
    
    for word in words:
        print(word