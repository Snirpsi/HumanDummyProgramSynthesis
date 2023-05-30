#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds all ports or converts a list of words. """    
    
    ports = input("Enter a ports list: ")
    ports = ports.split()
    
    ports_converted = []
    for port in ports:
        if port.isdigit():
            ports_converted.append(int(port))
        else:
            ports_converted.append(port)
    
    print(ports_converted)
    
