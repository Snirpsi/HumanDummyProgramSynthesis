#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port or adds all ports. """    
    while True:
        try:
            port = int(input("Enter a port number: "))
        except ValueError:
            print("Invalid port number")
        else:
            ports.add(port)
            print("Port number %d is now in use" % port)
            
