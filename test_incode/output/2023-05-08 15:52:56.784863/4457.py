#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that converts a list of numbers.
    import sys
    import http.server
    import socketserver

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(numbers)

    httpd = socketserver.TCPServer(("", 8000), Handler)
    httpd.serve_forever()

