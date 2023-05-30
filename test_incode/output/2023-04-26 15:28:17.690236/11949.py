#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a port or removes a port. """    
    port = int(input("Enter the port number you want to remove: "))
    
    if port == -1:
        print("The port number you entered was invalid.")
    else:
        remove_port(port)
        
