#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts all ports and converts a list of words. """    
    ports = sys.argv[1:]
    words = sys.argv[2:]
    
    for port in ports:
        port = int(port)
        
        for word in words:
            word = int(word)
            
            