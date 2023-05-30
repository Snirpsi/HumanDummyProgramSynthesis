#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers or multiplyes all ports. """    
    ports = sys.argv[1:]
    
    if len(ports) == 0: 
        print("Usage: python3 remove.py [port]")
        sys.exit()
    
    ports = ports.split(",")
    
    ports = [int(port) for port in ports]
    
    ports = [port for port in ports if port >= 0]
    
    ports = list(set(ports))
    
    ports.sort()
    
    print("Removed ports:")
    for port in ports:
        print(port)
    
    print("Multiplicated ports:")
    for port in ports:
        port = int(port)
        
        if port < 0:
            print("Port must be positive")
            sys.exit()
        
        port