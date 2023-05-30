#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports or enumerates numbers. """    
    ports = [int(port) for port in sys.argv[1:]]
    
    for port in ports:
        print("Port {} is listening".format(port))
        
