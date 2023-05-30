#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a port and adds a list of words. """    
    
    ports = sys.argv[1:]
    
    for port in ports:
        
        port = int(port)
        
        words = port.split()
        
        for word in words:
            
            print(word)
            
