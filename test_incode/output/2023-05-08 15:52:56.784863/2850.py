#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that prints user input.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn

    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes('<html><head><title>User Input</title></head>'
                                    '<body><p>User Input</p></body></html>', 'utf8'))

    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    ThreadingMixIn.instance().start()
    httpd.serve_forever()

