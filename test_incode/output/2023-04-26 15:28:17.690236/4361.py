#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports. """    
    ports = []
    
    # Start a server
    server = HTTPServer(('', 0), SimpleHTTPRequestHandler)
    
    # Start a thread to handle requests
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()
    
    # Wait until a port is available
    while True:
        ports.append(server.server_port)
        
        # Check if port is free
        if server.server_port in ports:
            break
    
    # Stop the server
    server.shutdown()
    
    # Close the thread
    thread.join()
    
    # Print the ports
    for port in ports:
        print('Port {} is free'.format(port))
    
