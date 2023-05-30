#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints user input or iterates over a port. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    while True:
        
        if port == -1:
            print("Please input a port number")
            continue
        
        if port == 0 or port == 65535:
            print("Please input a port number between 0 and 65535")
            continue
        
        print("Port number:", port)
        
        