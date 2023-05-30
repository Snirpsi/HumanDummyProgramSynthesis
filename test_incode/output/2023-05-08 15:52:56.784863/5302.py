#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that requests a list of words.
    #The words are then displayed in a web page.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            if parsed_url.path == "/":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes(
                    "<html><head><title>Words</title></head><body>",
                    "utf-8"))
                for word in words:
                    self.wfile.write(bytes(
                        "<p style=\"color: blue;\">%s</p>" % word,
                        "utf-8"))
                self.wfile.write(bytes(
                    "</body></html>",
                    "utf-8"))
            else:
                self.send_error(404)
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Handler)
    httpd.serve_forever()

