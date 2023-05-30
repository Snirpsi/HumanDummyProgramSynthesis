#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a port or prints a list of words. """    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 80
    
    words = []
    
    try:
        words.append(str(port))
    except TypeError:
        words.append(str(port))
    
    for word in words:
        print(word)
        
