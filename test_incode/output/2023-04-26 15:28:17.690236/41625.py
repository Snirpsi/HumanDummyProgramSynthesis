#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens all ports or calculates words. """    
    
    while True:
        
        # Open all ports
        openports()
        
        # Calculate words
        calcwords()
        
        # Sleep for 1 second
        time.sleep(1)
        
