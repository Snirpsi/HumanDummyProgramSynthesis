#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a port or prints words. """    
    
    ports = input("Enter the ports you want to remove: ")
    
    ports = ports.split()
    
    for port in ports:
        
        if port in ("help", "exit"):
            print("Usage: python3 remove-port.py port")
            
        elif port in ("port"):
            
            ports.remove(port)
            
            print("Port removed: " + port)
            
        elif port in ("all"):
            
            ports = ports + ports
            
            print("All ports removed")
            
        else:
            print("Invalid port number: " + port)
            
    print("Done")
    
