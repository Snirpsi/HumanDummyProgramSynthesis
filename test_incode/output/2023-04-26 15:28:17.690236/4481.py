#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes all ports. """    
    while True:
        ports = range(1,65535)
        ports.reverse()
        
        for port in ports:
            
            print("Port {} is now {}x".format(port,