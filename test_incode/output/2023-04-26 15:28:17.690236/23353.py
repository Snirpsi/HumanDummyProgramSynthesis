#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    
    # Create a webserver
    httpd = HTTPServer(("", 80), WordsHandler)
    
    # Start it
    httpd.serve_forever()
