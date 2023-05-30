#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers or returns a port. """    
    while True:
        port = input("Enter a port number: ")
        if port == "":
            print("No port number entered")
        else:
            remove_ports(port)
