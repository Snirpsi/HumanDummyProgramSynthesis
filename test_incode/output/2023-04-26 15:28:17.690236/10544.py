#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a port. """    
    
    # Get the port number from the command line
    port = int(sys.argv[1])
    
    # Get the port number from the configuration file
    port = int(config.get('main', 'port'))
    
    # Calculate the port number
    port = port + 2
    
    # Print the port number
    print('The port number is %d' % port)
    
    # Close the connection
    connection.close()
    
