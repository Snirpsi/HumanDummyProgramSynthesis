#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A function that enumerates a port.
    #It will print out a port number and a port name.
    #The port number is used to identify the port in other programs.
    #The port name is used to identify the port in other programs.
    portNumber = getPortNumber()
    portName = getPortName()
    print("Port Number: " + str(portNumber))
    print("Port Name: " + portName)

