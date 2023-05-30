#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A endless loop that requests all ports.
    while True:
        for port in ports:
            print(port)
        ports = range(0,65535)

