#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port or prints fruits. """    
    
    port = int(sys.argv[1])
    
    if port == 8080:
        print("Fruits served on port 8080")
    else:
        print("Fruits served on port " + str(port))
    
