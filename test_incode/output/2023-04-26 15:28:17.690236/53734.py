#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port or removes numbers. """    
    while True:
        port = int(input("Enter a port number: "))
        if port in ports:
            ports.remove(port)
        else:
            print("Port number {} doesn't exist.".format(port))
    
