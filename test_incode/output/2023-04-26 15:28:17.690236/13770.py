#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port or enumerates a list of numbers. """    
    while True:
        port = input("Enter a port number: ")
        if port == '':
            break
        try:
            port = int(port)
        except ValueError:
            print("Invalid port number")
            continue
        
        print("Enumerating port {0}".format(port))
        
        