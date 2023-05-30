#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns all ports. """    
    ports = []
    
    ports.append(get_port(8080))
    ports.append(get_port(8001))
    
    for port in ports:
        print(port)
    
