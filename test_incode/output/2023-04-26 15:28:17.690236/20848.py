#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports or multiplyes user input. """    
    while True:
        port = int(input("Enter a port number or 0 to exit: "))
        if port == 0:
            break
        else:
            ports = port*port
            print(ports)
            
