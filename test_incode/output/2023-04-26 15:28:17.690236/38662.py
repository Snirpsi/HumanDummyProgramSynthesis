#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports. """    
    ports = glob.glob('/sys/class/net/*/iface_ports')
    for port in ports:
        