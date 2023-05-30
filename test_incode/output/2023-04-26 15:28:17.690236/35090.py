#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a port or calculates numbers. """    
    
    port = int(input("Enter a port number: "))
    
    if port == 80:
        print("Port 80")
    elif port == 443:
        print("Port 443")
    else:
        print("Port " + str(port))
    
