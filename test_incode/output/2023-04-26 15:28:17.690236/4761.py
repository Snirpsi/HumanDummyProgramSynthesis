#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports. """    
    ports = open("/proc/net/tcp").read().splitlines()
    ports = [port.split(":")[0] for port in ports]
    ports = [port for port in ports if port]
    ports.sort()
    for port in ports:
        