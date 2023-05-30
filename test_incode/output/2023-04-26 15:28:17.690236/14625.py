#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words. """    
    
    # Start the server
    server = HTTPServer(('', 80), WordsHandler)
    
    # Start the webserver
    server.serve_forever()
    
