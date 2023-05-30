#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A function that converts all ports.
    ports = [str(p) for p in ports]
    ports = ','.join(ports)
    print(ports)

