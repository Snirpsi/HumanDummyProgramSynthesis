#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port or prints user input. """    
    port = int(sys.argv[1])
    
    if port == 0:
        print("No port specified")
    else:
        