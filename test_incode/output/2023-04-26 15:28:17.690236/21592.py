#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words. """    
    
    # Create a simple web server
    httpd = BaseHTTPServer.HTTPServer(('localhost', 8000), WordsHandler)
    
    # Start it
    httpd.serve_forever()
    
