#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports. """    
    ports = open("/proc/net/tcp")
    for port in ports:
        line = port.readline()
        if line.startswith("tcp"):
            line = line.split()
            port = int(line[1])
            