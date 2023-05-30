#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port. """    
    import sys
    from http.server import HTTPServer, BaseHTTPRequestHandler
    from socketserver import ThreadingMixIn
    from urllib.parse import urlparse, parse_qs
    from threading import Thread
    from random import randint
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            parsed_url = urlparse(self.path)
            query_dict = parse_qs(parsed_url.query)
            port = query_dict.get('port')
            
            if port is not None:
                port = int(port)
            else:
                port = randint(0, 65535)
            
            server_address = ('localhost', port)
            
            Thread(target=self.handle_request, args=(server_address,)).start()
            
    httpd = HTTPServer(server_address, MyHandler)
    httpd.serve_forever()

<|/ file ext=.py filename=server.py |>