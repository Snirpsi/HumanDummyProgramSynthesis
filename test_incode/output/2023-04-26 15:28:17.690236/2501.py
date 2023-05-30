#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits. """    
    
    # Create a simple webserver
    httpd = BaseHTTPServer.HTTPServer(('localhost', 8000), RequestHandler)
    
    # Start it
    httpd.serve_forever()
    
