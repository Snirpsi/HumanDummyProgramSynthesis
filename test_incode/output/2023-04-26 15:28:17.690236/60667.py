#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port or iterates over numbers. """    
    
    port = 8080
    
    # iterate over numbers
    for i in range(1,11):
        port = port + i
        
    # print port number
    print(port)
    
    # start webserver
    webserver.run(port=port)
    
