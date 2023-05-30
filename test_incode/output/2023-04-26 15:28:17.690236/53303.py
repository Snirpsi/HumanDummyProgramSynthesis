#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    from wsgiref.simple_server import make_server
    
    httpd = make_server('', 8000, MyApp)
    