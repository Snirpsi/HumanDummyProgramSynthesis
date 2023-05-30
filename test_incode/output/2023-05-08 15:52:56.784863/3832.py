#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A function that enumerates a port.
    #It will print out a line for each port number.
    #The port number will be the argument to the function.
    ports = enumeratePort(port)
    for port in ports:
        print(port)

