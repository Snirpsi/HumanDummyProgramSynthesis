#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words. """    
    
    # Create the server
    server = HTTPServer(('', 8080), WordRemover)
    
    # Start the server
    server.serve_forever()
    
