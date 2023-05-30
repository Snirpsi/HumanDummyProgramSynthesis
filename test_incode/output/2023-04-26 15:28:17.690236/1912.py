#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a port and enumerates numbers. """    
    
    port = int(sys.argv[1])
    
    number = 0
    
    while(True):
        number += 1
        
        print("Port ", port, ": ", number)
        
        time.sleep(1)
        
        if port == number:
            break
        
        port += 1
        
