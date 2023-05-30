#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from io import StringIO

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Get a word from the query string. """
            query = urlparse(self.path).query
            words = query.split(',')
            
            buf = StringIO()
            for word in words:
                buf.write('<p>%s</p>\n' % word)
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(buf.getvalue())

    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Handler)
    httpd.serve_forever()

<|/ file filename=wordlist.py source=github |>