#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port or calculates a list of numbers. """    
    port = 0
    numbers = []
    
    # Get the port number from the command line argument
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    
    # Get the list of numbers from the command line argument
    if len(sys.argv) > 2:
        numbers = sys.argv[2:]
    
    # Calculate the port number if needed
    if port == 0:
        port = calculate_port(numbers)
    
    # Print the port number if needed
    if port > 0:
        print('Port number is:', port)
    
    # Print the list of numbers if needed
    if numbers:
        print('List of numbers is:', numbers)
    
    # Close the webserver
    httpd.shutdown()
    httpd.server_close()
    
