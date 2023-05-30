#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port. """    
    while True:
        port = input("Enter the port to remove: ")
        
        if port == "":
            print("Port is empty")
        else:
            