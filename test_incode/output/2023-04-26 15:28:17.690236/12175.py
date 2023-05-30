#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers. """    
    from http.server import BaseHTTPRequestHandler
    from urllib.parse import parse_qs
    import socket
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            query = parse_qs(self.path.split('?')[1])
            
            if query['number']:
                number = query['number']
            else:
                number = 