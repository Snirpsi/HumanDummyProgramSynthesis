#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port or removes user input. """    
    
    # Start a web server
    server = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    # Wait forever
    server.serve_forever()
    
    # Stop the server
    server.socket.close()
    
    # Stop the web server
    