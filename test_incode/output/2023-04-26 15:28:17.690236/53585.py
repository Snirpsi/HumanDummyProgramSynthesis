#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of words or calculates all ports. """    
    
    words = sys.argv[1:]
    
    ports = []
    
    for word in words:
        
        ports.append(word)
        
    ports.sort()
    
    for port in ports:
        
        print(port)
        
