#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words or opens fruits. """    
    
    # Create a simple webserver
    httpd = BaseHTTPServer.HTTPServer(('localhost', 8080), RequestHandler)
    
    # Start it
    httpd.serve_forever()
    
