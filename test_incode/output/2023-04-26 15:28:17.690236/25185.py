#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port. """    
    while True:
        port = input("Enter a port: ")
        
        try:
            port = int(port)
        except ValueError:
            print("Invalid port")
            continue
        
        print("Converting port {} to {}".format(port, 