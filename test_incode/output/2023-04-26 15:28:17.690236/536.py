#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words. """    
    
    # Create a web server
    httpd = HTTPServer(('', 80), WordsHandler)
    
    # Start it
    httpd.serve_forever()
