#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words and enumerates all ports. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse, parse_qs
    from socketserver import ThreadingMixIn

    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            query = parse_qs(parsed_url.query)
            word = query.get('word')
            if word == '':
                word = 'word'
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(word