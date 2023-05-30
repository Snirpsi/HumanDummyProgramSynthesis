#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that enumerates user input.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from socketserver import ThreadingMixIn

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            if parsed_url.path == '/':
                sys.stdout.write('<html><body>')
                sys.stdout.write('<form action="/" method="post">')
                sys.stdout.write('<input type="text" name="user">')
                sys.stdout.write('<input type="submit" value="Submit">')
                sys.stdout.write('</form>')
                sys.stdout.write('</body></html>')
            else:
                sys.stdout.write('<html><body>')
                sys.stdout.write('<form action="/" method="post">')
                sys.stdout.write('<input type="text" name="user">')
                sys.stdout.write('<input type="submit" value="Submit">')
                sys.stdout.write('</form>')
                sys.stdout.write('</body></html>')

    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Handler)
    ThreadingMixIn.instance().start()
    httpd.serve_forever()

