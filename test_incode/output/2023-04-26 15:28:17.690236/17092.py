#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates user input and prints a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    ports = enumerate_ports(port)
    
    for port in ports:
        print("Port %i: " % port, end="")
        
        for letter in port:
            print(letter, end="")
            
        print("