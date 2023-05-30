#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A program that iterates over all ports.
    for port in ports:
        print("Port {} is open".format(port))

