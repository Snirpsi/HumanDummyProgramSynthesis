#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a port or enumerates user input. """    
    
    # Get the port number from the user
    port = int(input("Enter a port number: "))
    
    # Enumerate all available ports
    for port in range(1,65535):
        print(port)
    
    # 