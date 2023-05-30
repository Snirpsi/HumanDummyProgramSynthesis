#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a port and returns all ports. """    
    ports = []
    
    ports.append(8080)
    ports.append(8000)
    ports.append(9000)
    
    ports_multiply = []
    
    for port in ports:
        ports_multiply.append(port * 2)
    
    print(ports_multiply)
    
