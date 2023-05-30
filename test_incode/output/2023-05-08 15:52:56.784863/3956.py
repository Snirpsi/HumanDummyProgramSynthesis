#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A endless loop that enumerates all ports.
    while True:
        for port in ports:
            print(port)
        ports = ports[1:] + ports[0:1]

