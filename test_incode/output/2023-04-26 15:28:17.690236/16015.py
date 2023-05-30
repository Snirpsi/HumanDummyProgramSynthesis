#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port. """    
    while True:
        port = int(input("Enter a port number: "))
        
        if port == 9999:
            print("Exiting...")
            break
        else:
            print("Converting port {} to {}".format(port, 