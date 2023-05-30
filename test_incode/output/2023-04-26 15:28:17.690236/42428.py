#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores all ports or enumerates words. """    
    
    while True:
        ports = find_ports()
        words = get_words_from_ports(ports)
        
        for word in words:
            print(word)
        
        time.sleep(1)
        
