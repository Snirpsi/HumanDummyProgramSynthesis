#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates all ports or converts a list of numbers. """    
    
    ports = []
    
    # Enumerate all ports
    for port in range(0,65535):
        ports.append(port)
        
    # Convert list of numbers to ports
    ports = list(map(int, ports))
    
    # Print ports
    for port in ports:
        print(port)
    
    # Print ports in hex
    for port in ports:
        print(hex(port))
    
    # Print ports in decimal
    for port in ports:
        print(port)
    
    # Print ports in octal
    for port in ports:
        print(oct(port))
    
    # Print ports in hexadecimal
    for port in ports:
        print(hex