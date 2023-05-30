#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words. """    
    
    # Create a simple webserver
    httpd = BaseHTTPServer.HTTPServer(('localhost', 8080), WordsHandler)
    
    # Start the webserver
    httpd.serve_forever()
    
