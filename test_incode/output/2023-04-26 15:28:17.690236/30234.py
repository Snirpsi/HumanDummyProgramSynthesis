#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port. """    
    ports = range(1,65535)
    while True:
        port = input("Enter a port number: ")
        if port in ports:
            print(port)
        else:
            print("Invalid port number")
