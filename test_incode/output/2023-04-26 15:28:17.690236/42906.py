#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    httpd = BaseHTTPServer.HTTPServer(('localhost', 8080), WordsHandler)
    httpd.serve_forever()
