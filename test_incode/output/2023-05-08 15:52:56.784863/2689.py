#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A function that opens all ports.
    for port in ports:
        openport(port)

