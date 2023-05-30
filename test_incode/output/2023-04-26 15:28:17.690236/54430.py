#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words. """    
    
    # Create a simple webserver
    server = HTTPServer(('', 8000), WordsHandler)
    
    # Start the webserver
    server.serve_forever()
    
