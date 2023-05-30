#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a port or removes numbers. """    
    port = int(input("Enter a port number: "))
    
    if port > 0:
        print("The port number is:", port)
    else:
        print("The port number is:", 