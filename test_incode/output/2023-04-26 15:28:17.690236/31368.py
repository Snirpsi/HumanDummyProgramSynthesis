#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port. """    
    
    # Create a simple server
    server = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
    
    # Start the server
    server.serve_forever()
    
    # Stop the server
    server.socket.close()
    
