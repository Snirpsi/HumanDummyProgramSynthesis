#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of numbers or prints a port. """    
    ports = sys.argv[1:]
    
    if len(ports) == 0:
        print("Usage: python remove.py <ports>")
    else:
        for port in ports:
            remove_port(port)
            
