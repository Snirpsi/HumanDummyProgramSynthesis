#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port and removes all ports. """    
    while True:
        port = int(input("Enter a port number: "))
        
        if port < 0 or port > 65535:
            print("Invalid port number. Please try again.")
            continue
        
        ports.remove(port)
        
        print("Port number " + str(port) + " has been removed.")
        
        print("Press any key to exit.")
        
        input()
        
