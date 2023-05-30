#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port. """    
    while True:
        port = int(input("Enter a port number to remove: "))
        if port in ports:
            ports.remove(port)
            print("Port removed")
        else:
            print("Port not found")
