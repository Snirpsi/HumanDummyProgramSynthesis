#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports or iterates over numbers. """    
    
    ports = [int(port) for port in sys.argv[1:]]
    
    for port in ports:
        print("Port {} is open".format(port))
    
    for port in ports:
        