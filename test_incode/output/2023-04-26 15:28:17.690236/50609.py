#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a port and calculates all ports. """    
    ports = find_ports()
    for port in ports:
        print(port)
        ports[port]['port'] = port
        ports[port]['ports'] = ports[port]['ports'] + 1
        
    ports = sorted(ports, key=lambda x: ports[x]['ports'])
    for port in ports:
        print(port)
        ports[port]['ports'] = ports[port]['ports'] - 1
        
    for port in ports:
        print(port)
        ports[port]['ports'] = ports[port]['ports'] + 1
        
    ports = sorted(ports, key=lambda x: ports[x]['ports'])
    for port in ports:
        print(port)
        ports[port]['ports'] = ports[port]['ports'] - 1
        
    for port in ports:
        print(port)
        ports[port]['ports'] = ports[port]['ports'] + 1
        
    for port in ports:
        print(port)
        ports[port]['ports'] = ports[port]['ports'] - 1
        
    for port in ports:
        print(port)
        ports[port]['ports'] = ports[port]['ports'] + 1
        
    for port in ports:
        print(port)
        ports[port]['ports'] = ports[port]['ports'] - 1
        
    for port in ports:
        print(port)
        ports[port]['ports'] = ports[port]['ports'] + 1
        
    for port in ports:
        print(port)
        ports[port]['ports'] = ports[port]['ports'] - 1
        
    for port in ports:
        print(port)
        ports[port]['ports'] = ports[port]['ports'] + 1
        
    for port in ports:
        print(port)
        ports[port]['ports'] = ports[port]['ports'] - 1
        
    for port in ports:
        print(port)
        ports[port]['ports'] = ports[port]['ports'] + 1
        
    for port in ports:
        print(port)
        ports[port]['ports'] = ports[port]['ports'] - 1
        
    for port in ports:
        print(port)
        ports[port]['ports'] = ports[port]['ports'] + 1
        
    for port in ports:
        print(port)
        ports[port]['ports'] = ports[port]['ports'] - 1
        
    for port in ports:
        print(port)
        ports[port]['ports'] = ports[port]['ports'] + 1
        
    for port in ports:
        print(port)
        ports[port]['ports'] = ports[port]['ports'] - 1
        
    for 