#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports or prints numbers. """    
    
    ports = [int(p) for p in sys.argv[1:]]
    
    for port in ports:
        print("Port {} is open".format(port))
    
