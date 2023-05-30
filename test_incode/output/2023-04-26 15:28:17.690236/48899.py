#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over user input and calculates all ports. """    
    ports = []
    
    ports.append(input("Enter the port number for port A: "))
    ports.append(input("Enter the port number for port B: "))
    
    for port in ports:
        ports.append(int(port))
        
    print(ports)
    
