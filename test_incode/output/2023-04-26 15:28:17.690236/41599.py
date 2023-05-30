#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port. """    
    while True:
        port = input("Enter the port you want to remove: ")
        
        if port == "exit":
            break
        
        ports.remove(port)
        
        print("Port removed