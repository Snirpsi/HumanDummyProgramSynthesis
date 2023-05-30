#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words. """    
    
    # Create a server
    server = HTTPServer(('', 8080), WordsHandler)
    
    # Start the server
    server.serve_forever()
