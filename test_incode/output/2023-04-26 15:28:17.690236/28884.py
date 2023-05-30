#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port and iterates over all ports. """    
    
    ports = range(1,65535)
    
    while True:
        port = input("Enter a port number: ")
        
        if port in ports:
            print("Port {} is open.".format(port))
        else:
            print("Port {} is not open.".format(port))
        
        ports.remove(port)
        
