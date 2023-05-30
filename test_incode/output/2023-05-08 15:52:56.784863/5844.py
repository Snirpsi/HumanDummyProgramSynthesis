#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A program that adds all ports.
    ports = list(ports)
    ports.extend(range(65536,65536+len(ports)))
    print(ports)

