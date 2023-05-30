#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port. """    
    
    port = int(sys.argv[1])
    
    # Iterate over the port
    for port in range(port):
        print("Port {}".format(port))
        
    # Close the port
    port.close()
    
    # Close the program
    sys.exit()
