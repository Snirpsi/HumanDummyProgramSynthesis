#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port or multiplyes numbers. """    
    port = int(sys.argv[1])
    
    # Calculate the port number
    port = int(port * 2)
    
    # Multiply by 2
    port = port * 2
    
    # Print the port number
    print(port)
    
    # Run the server
    httpd = make_server('localhost', port, CalculatePort)
    httpd.serve_forever()
    
