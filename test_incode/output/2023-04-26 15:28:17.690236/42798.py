#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><head><title>Enumerate all ports</title></head>')
            self.wfile.write(b'<body>')
            self.wfile.write(b'<h1>Enumerate all ports</h1>')
            self.wfile.write(b'<p>')
            self.wfile.write(b'<i>This script will enumerate all available ports.</i>')
            self.wfile.write(b'</p>')
            self.wfile.write(b'</body></html>')
    
    httpd = HTTPServer(("", 0), MyHandler)
    httpd.serve_forever()
