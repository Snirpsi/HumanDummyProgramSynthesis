#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores all ports and enumerates user input. """    
    while True:
        ports = input("Enter ports separated by space: ")
        ports = ports.split()
        for port in ports:
            port = int(port)
            if port > 65535:
                print("Port number {} is out of range".format(port))
            else:
                