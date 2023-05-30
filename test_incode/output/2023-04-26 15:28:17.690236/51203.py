#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words. """    
    
    port = 8080
    
    # Create a server
    server = HTTPServer(('', port), WordsHandler)
    
    # Start the server
    server.serve_forever()
    
