#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts all ports. """    
    
    ports = sys.argv[1:]
    
    for port in ports:
        port = int(port)
        
        if port < 1 or port > 65535:
            print("Port {} is invalid.".format(port))
        else:
            port