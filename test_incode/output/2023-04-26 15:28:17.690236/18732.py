#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port and enumerates a list of numbers. """    
    while True:
        try:
            port = int(input("Enter a port number: "))
            ports.append(port)
        except:
            print("Invalid port number!")
            continue
        
