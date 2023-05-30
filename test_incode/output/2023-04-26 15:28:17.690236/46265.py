#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates all ports. """    
    ports = calc_ports(sys.argv[1])
    
    for port in ports:
        print(port)
    
