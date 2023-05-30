#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints all ports or removes user input. """    
    ports = input("Enter ports separated by comma: ").split(',')
    ports = [int(port) for port in ports]
    
    ports_removed = set()
    
    while True:
        ports_removed = ports_removed | set(ports)
        
        if ports_removed == ports:
            break
        
        print("Ports removed:", ports_removed)
        
        ports = input("Enter ports separated by comma: ").split(',')
        ports = [int(port) for port in ports]
        
    print("Ports removed:", ports_removed)
    
