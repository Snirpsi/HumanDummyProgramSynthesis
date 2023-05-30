#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens a port or prints fruits. """    
    
    port = sys.argv[1]
    
    if port == "open":
        open_fruits()
    elif port == "print":
        print_fruits()
    else:
        print("Invalid port")
        
