#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input. """    
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8000, application)
    httpd.serve_forever()