#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port. """    
    
    port = 8080
    
    # Create a server
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    # Wait forever
    server.serve_forever()
    
    # Close the server
    server.socket.close()
    
