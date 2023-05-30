#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port and stores all ports. """    
    while True:
        port = int(input("Enter a port to convert (1-65535): ")) 
        ports.append(port)
        
        print("Port ", port, "has been converted.")
        
        if port == 65535:
            break
    
    ports.sort()
    
    for port in ports:
        print(port)
    
