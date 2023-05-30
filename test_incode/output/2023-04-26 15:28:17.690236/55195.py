#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens numbers or prints a port. """    
    port = int(input("Enter a port number: "))
    
    if port == 80:
        print("Port 80")
    elif port == 443:
        print("Port 443")
    else:
        print("Port 