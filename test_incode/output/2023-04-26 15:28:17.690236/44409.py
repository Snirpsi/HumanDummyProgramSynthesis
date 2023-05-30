#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports or iterates over user input. """    
    
    ports = input("Enter ports: ")
    
    if ports == "exit":
        sys.exit()
    
    else:
        ports = ports.split(",")
        
        for port in ports:
            print(port)
            
