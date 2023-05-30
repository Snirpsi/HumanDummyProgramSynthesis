#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that opens fruits.txt and displays them in HTML
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from io import BytesIO
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urllib.parse.unquote(self.path)
            if path == "/":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<html><body>")
                for fruit in fruirs:
                    self.wfile.write(b"<h1>{}</h1>".format(fruit))
                self.wfile.write(b"</body></html>")
            else:
                self.send_error(404)
    server = HTTPServer(('', 8080), FruitHandler)
    server.serve_forever()

