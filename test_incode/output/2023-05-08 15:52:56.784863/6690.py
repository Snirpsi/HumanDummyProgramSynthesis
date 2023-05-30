#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A function that enumerates ports.
    ports = enumeratePorts(ports)
    #A function that prints all the ports.
    for port in ports:
        print(port)

