#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates all ports and multiplyes a list of numbers. """    
    
    ports = []
    
    while True:
        ports.append(int(input("Enter a port number: ")))
        
        if ports[-1] == 9999:
            break
        
    ports_multiplied = []
    
    for port in ports:
        ports_multiplied.append(port * 2)
        
    print(ports_multiplied)
    
    
