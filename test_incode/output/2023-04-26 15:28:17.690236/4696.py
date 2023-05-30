#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports and enumerates all ports. """    
    
    ports = enumerate_ports()
    
    for port in ports:
        print("Port {} is {}".format(port, ports[port]))
    
    print("\nDone")
    
