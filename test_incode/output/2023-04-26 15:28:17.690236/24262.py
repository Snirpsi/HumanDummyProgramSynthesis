#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts words and iterates over all ports. """    
    ports = range(1,65535)
    
    while True:
        word = ''
        
        for port in ports:
            word = word + chr(port)
            
        print('Sending "%s" over port %s...' % (word, port))
        
        