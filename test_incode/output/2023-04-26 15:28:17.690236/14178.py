#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of numbers or adds a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python add_ports.py <ports>")
        sys.exit()
    
    ports = sys.argv[1:]
    
    for port in ports:
        add_port(port)
    
    print("Done!")
    
