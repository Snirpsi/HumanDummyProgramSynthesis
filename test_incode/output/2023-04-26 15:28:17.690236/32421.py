#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words. """    
    words = []
    
    # Create a server and listen on port 80
    server = HTTPServer(('', 80), WordsHandler)
    
    # Start a thread to serve the request
    server.serve_forever()
