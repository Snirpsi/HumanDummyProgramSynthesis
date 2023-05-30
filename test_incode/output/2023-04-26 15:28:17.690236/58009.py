#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words or returns all ports. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <word>" % sys.argv[0])
        sys.exit()
    
    word = sys.argv[1]
    
    ports = find_ports(word)
    
    for port in ports:
        print(port)
    
