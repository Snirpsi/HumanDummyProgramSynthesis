#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port or iterates over a list of numbers. """    
    
    port = 1
    
    while True:
        port = port + 1
        print('Port is', port)
        
        if port > 65535:
            print('Port is too high.')
            break
        
        if port % 2 == 0:
            print('Port is even.')
        else:
            print('Port is odd.')
            
        print('Press ENTER to exit.')
        
        input()
        
