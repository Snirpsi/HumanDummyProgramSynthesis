#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers and prints a list of words. """    
    import sys
    from wsgiref.simple_server import make_server
    
    httpd = make_server('', 8080, WordsApp)
    httpd.serve_forever()
    
