#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    import sys
    from wsgiref.simple_server import make_server
    
    port = 8000
    
    httpd = make_server('localhost', port, WordsHandler)
    httpd.serve_forever()
    
