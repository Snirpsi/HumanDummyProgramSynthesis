#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words. """    
    
    # Create the server
    server = HTTPServer(('', 8000), WordsHandler)
    
    # Start the server
    server.serve_forever()
    
