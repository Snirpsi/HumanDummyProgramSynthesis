#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports or adds user input. """    
    
    ports = input("Enter ports (comma separated): ")
    ports = ports.split(",")
    
    for port in ports:
        
        port = int(port)
        
        if port < 0 or port > 65535:
            print("Port number must be between 0 and 65535.")
        else:
            
            print("Port number " + str(port) + " is now open.")
            
