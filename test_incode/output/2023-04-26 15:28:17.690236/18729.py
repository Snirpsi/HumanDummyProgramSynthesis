#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words. """    
    
    # Start a server
    httpd = HTTPServer(('', 8080), WordsHandler)
    
    # Start a web server
    httpd.serve_forever()
