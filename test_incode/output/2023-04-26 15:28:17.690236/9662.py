#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words. """    
    
    words = []
    
    # Create a simple webserver
    httpd = HTTPServer(('', 8000), WordsHandler)
    
    # Start it
    httpd.serve_forever()
