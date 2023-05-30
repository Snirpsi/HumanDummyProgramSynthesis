#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words or enumerates fruits. """    
    from wsgiref.simple_server import make_server
    
    make_server('localhost', 8080, WordsApp