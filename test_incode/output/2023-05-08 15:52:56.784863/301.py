#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A endless loop that calculates all ports.
    while True:
        ports = ports + range(0,65535)
        ports = list(set(ports))
        ports.sort()
        for port in ports:
            print(port)

