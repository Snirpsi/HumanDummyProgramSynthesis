#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port and removes numbers. """    
    port = int(sys.argv[1])
    
    # Remove all numbers from port and print result
    remove_numbers(port)
    
    # Print the port number
    print('Port number: ' + str(port))
    
    # Close the server
    server.socket.close()
    
    # Close the program
    