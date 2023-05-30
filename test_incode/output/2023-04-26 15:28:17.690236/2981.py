#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens user input or converts all ports. """    
    
    ports = input("Enter ports separated by commas (no spaces): ")
    ports = ports.split(",")
    
    ports = [int(port) for port in ports]
    
    for port in ports:
        
        if port < 0 or port > 65535:
            print("Port number must be between 0 and 65535.")
            continue
        
        if port == 0 or port == 65535:
            
            print("Port number must be between 0 and 65535.")
            continue
        
        