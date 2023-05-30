#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that adds user input.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs
    import cgi

    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(
                '<html><head><title>User Input</title></head>'
                '<body>'
                '<form action="/" method="post">'
                '<input name="name" type="text">'
                '<input name="age" type="text">'
                '<input name="submit" type="submit">'
                '</form>'
                '</body></html>'
                )

    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()

