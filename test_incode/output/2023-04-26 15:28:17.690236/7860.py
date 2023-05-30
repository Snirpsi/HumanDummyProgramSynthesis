#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns user input or returns a port. """    
    import sys
    port = int(sys.argv[1])
    
    if port == -1:
        print("Please provide a port number.")
    else:
        print("You chose port number " + str(port))
        
