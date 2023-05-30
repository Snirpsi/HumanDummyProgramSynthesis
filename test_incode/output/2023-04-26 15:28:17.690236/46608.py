#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port. """    
    port = 8080
    
    # Create a server to listen on port 8080
    httpd = HTTPServer(('', port), Handler)
    
    # Start the server
    httpd.serve_forever()
    
    # Stop the server
    httpd.server_close()
    
