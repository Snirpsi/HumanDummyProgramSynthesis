#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers or enumerates a port. """    
    while True:
        port = int(input("Enter a port number: "))
        
        if port == -1:
            break
        
        if port < 0 or port > 65535:
            print("Invalid port number")
            continue
        
        print("Converting port %d to hexadecimal" % port)
        
        hexadecimal = bin(port)[2:]
        
        print("Hexadecimal port number: %s" % hexadecimal)
        
        print("Enumerating ports")
        
        for port in range(port, 65535):
            print("Port %d = %s" % (port, bin(port)[2:]))
            
        print("Done")
        
