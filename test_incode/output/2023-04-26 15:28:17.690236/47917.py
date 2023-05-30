#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers. """    
    
    httpd = HTTPServer(('localhost', 8080), NumbersHandler)
    httpd.serve_forever()
    
