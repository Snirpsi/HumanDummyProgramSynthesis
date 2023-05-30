#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words. """    
    import sys
    from wsgiref.simple_server import make_server
    from words import Words
    
    httpd = make_server('localhost', 8080, Words)
    print('Serving on port 8080')
    httpd.serve_forever()
    
