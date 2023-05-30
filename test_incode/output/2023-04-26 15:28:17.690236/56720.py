#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns all ports and returns words. """    
    ports = find_ports()
    words = find_words()
    
    for port in ports:
        for word in words:
            print(port + 