#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a port. """    
    
    port = int(input("Enter a port number: "))
    
    if port == 80:
        print("The port is 80")
    elif port == 443:
        print("The port is 443")
    elif port == 8080:
        print("The port is 8080")
    elif port == 444:
        print("The port is 444")
    elif port == 8888:
        print("The port is 8888")
    elif port == 9999:
        print("The port is 9999")
    elif port == 99999:
        print("The port is 99999")
    else:
        print("The port is invalid")
    
