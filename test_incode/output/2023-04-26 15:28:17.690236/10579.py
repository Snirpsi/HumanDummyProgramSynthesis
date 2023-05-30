#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports or adds a list of words. """    
    
    ports = enumerate_ports()
    
    for port in ports:
        
        words = get_words(port)
        
        for word in words:
            print(word)
    
