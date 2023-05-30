#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a port or adds all ports. """    
    ports = sys.argv[1:]
    
    for port in ports:
        port = int(port)
        
        if port > 0:
            ports.append(port)
        else:
            ports.insert(0, port)
            
    print(ports)
    
