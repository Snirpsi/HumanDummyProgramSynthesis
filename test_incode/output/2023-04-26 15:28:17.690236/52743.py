#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words. """    
    
    # Create a server
    server = HTTPServer(('', 8000), WordsHandler)
    
    # Start the server
    server.serve_forever()

