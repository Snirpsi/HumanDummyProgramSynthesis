#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports or stores a list of words. """    
    
    ports = Ports()
    ports.start()
    
    words = []
    
    while True:
        words.append(ports.read())
        
        print(' '.join(words))
        
        ports.