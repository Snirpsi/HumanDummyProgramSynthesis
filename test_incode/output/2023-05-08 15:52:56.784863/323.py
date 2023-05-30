#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that opens fruits.txt and displays them
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from io import BytesIO
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = self.wfile.read()
            self.wfile.write(bytes(html, 'utf-8'))
    server = HTTPServer(('', 8000), RequestHandler)
    server.serve_forever()

