#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words. """    
    import sys
    from wsgiref.simple_server import make_server
    from wsgiref.simple_server import WSGIRequestHandler
    from wsgiref.simple_server import make_handler_with_log
    from wsgiref.simple_server import make_error_handler_with_log

    words = []
    for line in sys.stdin:
        words.append(line.strip())

    server_address = ('localhost', 8000)
    httpd = make_server(server_address, WSGIRequestHandler, words=words)
    httpd.serve_forever()

