#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words. """    
    import sys
    from wsgiref.simple_server import make_server
    
    httpd = make_server('', 8000, WordsApp)
    httpd.serve_forever()

<|/ file source=github filename=word