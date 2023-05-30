#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A endless loop that returns all ports.
    while True:
        ports.clear()
        for port in ports:
            print(port)
        ports.clear()
        ports.extend((port + 1 for port in range(65536)))

