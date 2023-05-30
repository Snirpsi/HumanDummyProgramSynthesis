#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a port. """    
    port = int(sys.argv[1])
    
    if port == 8080:
        print("Port 8080 was found!")
    else:
        print("Port {} was not found!".format(port))
    
