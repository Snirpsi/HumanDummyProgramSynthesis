#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that returns user input.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs

    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            query = parse_qs(
                self.path.split('?')[1],
                keep_blank_values=True
            )
            query = dict(query)
            query = query.get('q')
            if query:
                query = query.replace(' ', '+')
                self.wfile.write(query)
            else:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

    server = HTTPServer(('', 8080), RequestHandler)
    server.serve_forever()

