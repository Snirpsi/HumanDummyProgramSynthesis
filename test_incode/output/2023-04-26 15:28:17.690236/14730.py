#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    
    words = []
    
    # Create a simple HTTP server
    httpd = HTTPServer(('', 8080), WordsHandler)
    
    # Start it
    httpd.serve_forever()
    
