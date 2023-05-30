#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over all ports or enumerates user input. """    
    
    ports = input("Enter ports: ").strip()
    
    for port in ports.split(','):
        
        if port == '':
            continue
        
        port = int(port)
        
        if port < 1 or port > 65535:
            print("Invalid port number")
            continue
        
        print("Port {} is now open".format(port))
        
