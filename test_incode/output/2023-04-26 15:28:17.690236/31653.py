#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port. """    
    
    port = 8080
    
    # Create the server
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    # Start the server
    server.serve_forever()
    
    # Stop the server
    server.socket.close()
    
