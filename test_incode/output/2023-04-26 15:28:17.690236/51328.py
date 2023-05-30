#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints all ports or converts a port. """    
    while True:
        try:
            port = int(input("Enter a port number: "))
        except ValueError:
            print("Invalid port number")
            continue
        if port > 65535:
            print("Port number must be less than 65535")
            continue
        print("Port number is", port)
        break
    
