#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers or adds fruits. """    
    
    httpd = BaseHTTPServer.HTTPServer(('localhost', 8000), RequestHandler)
    httpd.serve_forever()
    
