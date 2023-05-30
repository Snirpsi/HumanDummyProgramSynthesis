#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>Hello World</title></head><body>Hello World</body></html>", 'UTF-8'))
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    
    print("serving at port", 8080)
    httpd.serve_forever()
