#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A function that calculates all ports.
    ports = list(set(ports))
    ports.sort()
    for port in ports:
        print(port)

