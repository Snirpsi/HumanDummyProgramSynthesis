#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words and enumerates all ports. """    
    from wsgiref.simple_server import make_server
    
    httpd = make_server('', 8000, MyApp)
    httpd.serve_forever()
