#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port. """    
    
    port = 1
    
    while True:
        
        port = port + 1
        
        print("Port {} is open".format(port))
        
        time.sleep(1)
        
