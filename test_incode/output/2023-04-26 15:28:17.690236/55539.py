#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words. """    
    
    # Create a simple web server
    httpd = BaseHTTPServer.HTTPServer(('localhost', 8000), WordsHandler)
    
    # Start the web server
    httpd.serve_forever()
    
