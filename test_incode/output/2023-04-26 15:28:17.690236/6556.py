#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a port. """    
    port = int(sys.argv[1])
    
    ports.remove(port)
    
    print("Removed port " + str(port))
    
