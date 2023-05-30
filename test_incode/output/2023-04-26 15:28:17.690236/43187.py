#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a port or enumerates user input. """    
    
    ports = input("Enter a list of ports to remove: ")
    ports = ports.split()
    
    for port in ports:
        
        if port == "all":
            
            ports.remove("all")
            
        else:
            
            ports.remove(port)
            
    ports = list(set(ports))
    
    print("\n".join(ports))
    
