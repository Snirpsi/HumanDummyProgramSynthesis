#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and converts words. """    
    port = sys.argv[1]
    
    words = []
    
    while True:
        
        words.append(str(port))
        
        port = port + 1
        
        if port > 65535:
            port = 65535
            
    words.sort()
    
    print('\n'.join(words))
    
