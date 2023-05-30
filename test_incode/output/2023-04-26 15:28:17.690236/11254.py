#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port and stores all ports. """    
    while True:
        port = int(input("Enter a port number: "))
        ports.append(port)
        print("Port number {} has been added.".format(port))
        
