#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A function that requests ports.
    ports = requestPorts(ports)
    #A function that prints ports.
    print(ports)

