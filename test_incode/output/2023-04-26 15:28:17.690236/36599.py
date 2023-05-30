#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words and adds a list of words. """    
    import sys
    from wsgiref.simple_server import make_server
    
    wordlist = sys.argv[1:]
    
    httpd = make_server('localhost', 8080, Words