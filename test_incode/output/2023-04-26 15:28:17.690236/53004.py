#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    from wsgiref.simple_server import make_server
    
    httpd = make_server('localhost', 8080, MyHandler)
    httpd.serve_forever()
