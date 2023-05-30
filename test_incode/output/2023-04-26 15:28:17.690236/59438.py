#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes words and converts all ports. """    
    import sys
    
    words = [line.strip() for line in sys.stdin]
    
    words = [word.upper() for word in words]
    
    words = [word.lower() for word in words]
    
    words = [word for word in words if word != ""]
    
    words = [word for word in words if word != "