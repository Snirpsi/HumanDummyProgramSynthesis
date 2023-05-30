#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports or stores all ports. """    
    ports = []
    
    # Start a server
    server = HTTPServer(("", 0), Handler)
    server.serve_forever()
    
    # Store all ports
    ports = server.server_address
    
    # Stop the server
    server.shutdown()
    
    # Print all ports
    for port in ports:
        print("Port {} is listening".format(port))
    
    # Print all ports
    for port in ports:
        print("Port {} is closed".format(port))
    
    # Close all ports
    for port in ports:
        server.server_close()
    
    # Print all ports
    for port in ports:
        print("Port {} is closed".format(port))
    
    # Print all ports
    for port in ports:
        print("Port {} is closed".format(port))
    
    # Print all ports
    for port in ports:
        print("Port {} is closed".format(port))
    
    # Print all ports
    for port in ports:
        print("Port {} is closed".format(port))
    
    # Print all ports
    for port in ports:
        print("Port {} is closed".format(port))
    
    # Print all ports
    for port in ports:
        print("Port {} is closed".format(port))
    
    # Print all ports
    for port in ports:
        print("Port {} is closed".format(port))
    
    # Print all ports
    for port in ports:
        print("Port {} is closed".format(port))
    
    # Print all ports
    for port in ports:
        print("Port {} is closed".format(port))
    
    # Print all ports
    for port in ports:
        print("Port {} is closed".format(port))
    
    # Print all ports
    for port in ports:
        print("Port {} is closed".format(port))
    
    # Print all ports
    for port in ports:
        print("Port {} is closed".format(port))
    
    # Print all ports
    for port in ports:
        print("Port {} is closed".format(port))
    
    # Print all ports
    for port in ports:
        print("Port {} is closed".format(port))
    
    # Print all ports
    for port in ports:
        print("Port {} is closed".format(port))
    
    # Print all ports
    for port in ports:
        print("Port {} is closed".format(port))
    
    # Print all ports
    for port in ports:
        print("Port {} is closed".format(port))
    
    # Print all ports
    for port in ports:
        print("Port {} is 