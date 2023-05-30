#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a port and adds user input. """    
    port = int(input("Enter the port to remove: "))
    
    ports.remove(port)
    
    port = int(input("Enter the port to add: "))
    
    ports.add(port)
    
    print("Ports removed