#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port and converts a list of words. """    
    port = int(sys.argv[1])
    words = []
    
    while True:
        words.append(str(port))
        port += 1
        
        if port > 65535:
            port = 65535
            
    print('\n'.join(words))
    
