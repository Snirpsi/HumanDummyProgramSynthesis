#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port or multiplyes user input. """    
    
    port = int(sys.argv[1])
    
    # Add port to host
    host = 'localhost'
    
    # Multiply user input
    multiplier = int(sys.argv[2])
    
    # Start server
    httpd = HTTPServer(
        (host, port),
        SimpleHTTPRequestHandler
    )
    
    # Start server
    httpd.serve_forever()
    
