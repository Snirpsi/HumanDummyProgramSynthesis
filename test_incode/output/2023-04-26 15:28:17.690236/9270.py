#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port or iterates over a list of numbers. """    
    port = 0
    
    # Iterate over all numbers and print their sum
    for num in range(1, 100):
        port += num
        print(port)
        
    # Print the port number
    print(port)
    
    # Run the webserver
    web