#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports and enumerates a list of words. """    
    
    ports = enumeratePorts()
    
    words = []
    for port in ports:
        words.append(getWord(port))
    
    print(words)
    
