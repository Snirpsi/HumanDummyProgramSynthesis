#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers or removes all ports. """    
    ports = input("Enter a port: ")
    ports = ports.split()
    ports = ports[:]
    ports.sort()
    ports = ports[0:]
    
    ports_open = []
    
    for port in ports:
        if port not in ports_open:
            ports_open.append(port)
            
    ports_open = ports_open[::-1]
    
    for port in ports_open:
        print("Port {} is open.".format(port))
    
    ports_open = input("Enter a port: ")
    ports_open = ports_open.split()
    ports_open = ports_open[::-1]
    
    ports_open = ports_open[0:]
    
    for port in ports_open:
        if port in ports_open:
            print("Port {} is open.".format(port))
        else:
            print("Port {} is not open.".format(port))
    
    ports_open = input("Enter a port: ")
    ports_open = ports_open.split()
    ports_open = ports_open[::-1]
    
    ports_open = ports_open[0:]
    
    for port in ports_open:
        if port in ports_open:
            print("Port {} is open.".format(port))
        else:
            print("Port {} is not open.".format(port))
    
    ports_open = input("Enter a port: ")
    ports_open = ports_open.split()
    ports_open = ports_open[::-1]
    
    ports_open = ports_open[0:]
    
    for port in ports_open:
        if port in ports_open:
            print("Port {} is open.".format(port))
        else:
            print("Port {} is not open.".format(port))
    
    ports_open = input("Enter a port: ")
    ports_open = ports_open.split()
    ports_open = ports_open[::-1]
    
    ports_open = ports_open[0:]
    
    for port in ports_open:
        if port in ports_open:
            print("Port {} is open.".format(port))
        else:
            print("Port {} is not open.".format(port))
    
    ports_open = input("Enter a port: ")
    ports_open = ports_open.split()
    ports_open = ports_open[::-1]
    
    ports_open = ports_open[0:]
    
    for port in ports_open:
        if port in ports_open:
            print("Port {} is open.".format(port))
        else:
            print("Port {} is not open.".format(port))
    
    ports_open