#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words and opens a port. """    
    
    # Create a simple webserver
    httpd = HTTPServer(("", 80), WordsHandler)
    
    # Start a web server
    httpd.serve_forever()
    
