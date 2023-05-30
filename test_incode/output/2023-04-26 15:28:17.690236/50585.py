#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a port or opens a list of numbers. """    
    
    ports = input("Enter a list of ports separated by commas e.g. '1,3,5'\n").split(',')
    
    for port in ports:
        port = int(port)
        
        if port > 65535:
            print("Port number must be less than 65535.")
        else:
            ports.append(port)
    
    print(ports)
    
