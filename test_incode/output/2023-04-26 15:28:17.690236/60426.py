#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports and iterates over user input. """    
    
    ports = []
    
    # Iterate over all ports
    for port in range(0, 65535):
        ports.append(port)
    
    # Iterate over user input
    while True:
        port = int(input("Enter a port number: "))
        
        if port in ports:
            print("Port number " + str(port) + " is open.")
        else:
            print("Port number " + str(port) + " is not open.")
            
