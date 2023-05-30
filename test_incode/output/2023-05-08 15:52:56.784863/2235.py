#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A program that iterates over all ports.
    #It then prints out the port number and the port name.
    for port in ports:
        print(port,"is listening on port ",port)

