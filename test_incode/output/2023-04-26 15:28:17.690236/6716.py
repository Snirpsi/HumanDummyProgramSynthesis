#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words and returns all ports. """    
    import sys
    
    words = []
    ports = []
    
    for arg in sys.argv[1:]:
        if arg == '-':
            continue
        
        words = arg.split(' ')
        
        for word in words:
            ports.append(word)
    
    for port in ports:
        print('{:<20} {:<20} {:<20}'.format(port, port, port))
    
