#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers or removes all ports. """    
    ports = sys.argv[1:]
    ports = [int(port) for port in ports]
    
    if len(ports) == 1:
        ports = ports[0]
    
    ports = [port for port in ports if port > 0]
    
    if len(ports) == 1:
        ports = ports[0]
    
    ports = [port for port in ports if port < 65535]
    
    if len(ports) == 1:
        ports = ports[0]
    
    ports = [port for port in ports if port > 65535]
    
    if len(ports) == 1:
        ports = ports[0]
    
    ports = [port for port in ports if port != 0]
    
    if len(ports) == 1:
        ports = ports[0]
    
    ports = [port for port in ports if port != 65535]
    
    if len(ports) == 1:
        ports = ports[0]
    
    ports = [port for port in ports if port != 65536]
    
    if len(ports) == 1:
        ports = ports[0]
    
    ports = [port for port in ports if port != 65537]
    
    if len(ports) == 1:
        ports = ports[0]
    
    ports = [port for port in ports if port != 65538]
    
    if len(ports) == 1:
        ports = ports[0]
    
    ports = [port for port in ports if port != 65539]
    
    if len(ports) == 1:
        ports = ports[0]
    
    ports = [port for port in ports if port != 655