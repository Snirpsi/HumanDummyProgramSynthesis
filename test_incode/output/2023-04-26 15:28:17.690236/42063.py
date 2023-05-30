#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input. """    
    from wsgiref.simple_server import make_server
    import sys
    
    httpd = make_server('localhost', 8000, UserInputHandler)
    httpd.serve_forever()
    
