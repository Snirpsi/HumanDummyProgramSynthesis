#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A function that opens all ports.
    ports = [int(p) for p in sys.argv[1:]]
    ports = list(set(ports))
    ports.sort()
    for port in ports:
        openport(port)

