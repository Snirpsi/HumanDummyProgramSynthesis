#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A endless loop that converts all ports.
    while True:
        for port in ports:
            ports[port] = ports[port] + 1
        print(ports)

