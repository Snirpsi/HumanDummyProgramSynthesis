#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that stores fruits.
    #This example is for illustrative purposes only.
    #Feel free to point out any flaws in this code.
    import os
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    import json

    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == "/":
                path = os.path.join(os.path.dirname(__file__), "index.html")
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(open(path).read())

    server = HTTPServer(('', 8080), RequestHandler)
    server.serve_forever()

