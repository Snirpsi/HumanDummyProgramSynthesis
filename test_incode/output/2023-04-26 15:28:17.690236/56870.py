#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts all ports and stores a port. """    
    while True:
        port = int(input("Enter a port (1-65535): "))
        if port > 65535:
            print("Port number must be between 1 and 65535.")
        else:
            ports.append(port)
            
