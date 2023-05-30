#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port and enumerates user input. """    
    while True:
        port = input("Enter a port number: ")
        if port == '':
            break
        
        print("Enumerating ports starting with port number", port)
        
        ports = enumerate_ports(port)
        for port in ports:
            print("Port number", port, "is available.")
        
        print("\nPress enter to exit.")
        
        