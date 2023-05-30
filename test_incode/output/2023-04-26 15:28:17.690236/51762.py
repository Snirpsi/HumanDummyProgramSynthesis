#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words. """    
    import sys
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8080, WordsApp)
    httpd.serve_forever()