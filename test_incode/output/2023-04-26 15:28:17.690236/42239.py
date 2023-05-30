#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port and calculates numbers. """    
    port = int(input("Enter a port number: "))
    
    ports = [port]
    
    while True:
        ports.append(int(input("Enter a port number: ")))
        
        if port == ports[-1]:
            break
        
        ports.append(ports[-1] + 