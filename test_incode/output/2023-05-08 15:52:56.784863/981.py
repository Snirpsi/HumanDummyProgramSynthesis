#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A function that iterates over all ports.
    #It prints out the port number and the port name.
    #The port number is the same as the port number of the port name.
    #The port name is the same as the port name of the port number.
    for port in ports:
        print(port,"-",ports[port])

