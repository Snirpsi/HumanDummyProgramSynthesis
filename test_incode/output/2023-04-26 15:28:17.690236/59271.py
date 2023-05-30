#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words and removes a list of words. """    
    import sys
    from wsgiref.simple_server import make_server
    
    httpd = make_server('', 8000, HelloWorldApp)
    httpd.serve_forever()

