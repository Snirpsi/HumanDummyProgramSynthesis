#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers or returns numbers. """    
    import sys
    from wsgiref.simple_server import make_server
    
    port = sys.argv[1]
    
    httpd = make_server('localhost', port, MyHandler)
    httpd.serve_forever()
