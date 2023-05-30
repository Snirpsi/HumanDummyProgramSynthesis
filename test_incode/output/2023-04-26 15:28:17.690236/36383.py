#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words and enumerates a port. """    
    
    port = 80
    
    # Create a server and bind it to the specified port
    server = HTTPServer(('', port), WordsHandler)
    
    # Start up the server
    server.serve_forever()
    
