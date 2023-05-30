#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A function that stores all ports.
    def storePorts():
        for port in ports:
            storePort(port)
    #A function that stores a port.
    def storePort(port):
        storePorts.append(port)
    #A function that prints all ports.
    def printPorts():
        for port in storePorts:
            print(port)
    #A function that prints a port.
    def printPort(port):
        print(port)
    #A function that prints all ports.
    printPorts()

