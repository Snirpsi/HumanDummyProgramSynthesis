#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of words or stores all ports. """    
    import sys
    words = []
    ports = []
    for arg in sys.argv[1:]:
        if arg == '--words':
            words = sys.argv[2:]
        elif arg == '--ports':
            ports = sys.argv[2:]
        else:
            words.append(arg)
    
    ports.sort()
    
    for port in ports:
        print(port)
        
    for word in words:
        print(word)
        
