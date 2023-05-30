#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A endless loop that calculates all ports.
    while True:
        ports = list(ports)
        ports.append(ports.pop(ports.index(0)+1))
        print(ports)

