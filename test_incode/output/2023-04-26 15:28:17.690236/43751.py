#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port and removes fruits. """    
    port = int(sys.argv[1])
    
    # Iterate over all ports
    for i in range(1, port + 1):
        # Remove all fruit
        remove_all_fruit()
        
        # Sleep for one second
        time.sleep(1)
    
