#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports or multiplyes a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python words_to_ports.py <words>')
        exit()
    
    words = sys.argv[1:]
    
    for word in words:
        ports = words_to_ports(word)
        
        for port in ports:
            print(port)
        
