#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers or stores words. """    
    
    port = 8080
    
    # Create a server
    server = HTTPServer(('', port), RequestHandler)
    
    # Start the server
    server.serve_forever()
    
