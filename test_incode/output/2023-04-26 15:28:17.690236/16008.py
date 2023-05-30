#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port and enumerates all ports. """    
    while True:
        port = input("Enter a port number: ")
        ports.append(port)
        print("Port number:", port)
        
        # Enumerate all ports
        for port in ports:
            print(port)
        
        # 