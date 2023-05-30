#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    ports = range(0,65535)
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            for port in ports:
                self.wfile.write(str(port))
    
    httpd = HTTPServer(("", 0), MyHandler)
    httpd.serve_forever()
    
