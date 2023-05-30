#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers. """    
    
    httpd = HTTPServer(('', 80), NumberHandler)
    httpd.serve_forever()
    
