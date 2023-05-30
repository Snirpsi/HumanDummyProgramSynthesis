#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    from wsgiref.simple_server import make_server
    
    words = []
    for line in sys.stdin:
        words.append(line.strip())
    
    httpd = make_server('localhost', 8080, MyApp)
    httpd.serve_forever()

