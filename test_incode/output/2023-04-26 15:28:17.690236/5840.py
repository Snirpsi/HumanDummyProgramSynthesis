#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words. """    
    import sys
    from wsgiref.simple_server import make_server
    from wsgiref.simple_server import WSGIRequestHandler
    from wsgiref.simple_server import make_handler
    from wsgiref.simple_server import make_error_page
    
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    server = make_server('localhost', 8000, WSGIRequestHandler)
    
    server.serve_forever()
    
if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1:
        words = [sys.argv[1]]
    
    words.sort()
    
    