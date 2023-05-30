#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port or opens numbers. """    
    while True:
        try:
            port = int(input("Enter a port number: "))
            openPorts(port)
        except KeyboardInterrupt:
            break
