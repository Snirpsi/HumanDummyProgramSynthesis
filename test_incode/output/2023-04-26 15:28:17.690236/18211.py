#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints a port or opens a port. """    
    port = None
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = input("Enter a port number: ")
    
    if port == "open":
        openPort()
    elif port == "print":
        printPort()
    else:
        print("Invalid port number")
        
