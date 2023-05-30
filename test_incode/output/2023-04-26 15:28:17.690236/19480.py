#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port and multiplyes user input. """    
    port = int(input("Enter a port number: "))
    
    for port in range(1,port+1):
        print("Port number {} is {}.".format(port, port * 