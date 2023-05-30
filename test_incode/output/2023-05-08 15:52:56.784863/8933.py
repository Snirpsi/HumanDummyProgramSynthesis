#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A program that calculates all ports.
    ports = list(ports)
    ports.sort()
    for port in ports:
        print(port)

