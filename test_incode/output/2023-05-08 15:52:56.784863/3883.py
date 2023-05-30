#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that converts words.txt into html and serves it.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import socketserver

    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('words.txt', 'r') as file:
                for line in file:
                    self.wfile.write(line)

    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    httpd.serve_forever()

