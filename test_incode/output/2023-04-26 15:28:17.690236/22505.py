#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input and removes a port. """    
    while True:
        port = input("Enter a port number: ")
        
        if port == "":
            print("Port number cannot be empty")
            continue
        
        remove_port(port)
        
