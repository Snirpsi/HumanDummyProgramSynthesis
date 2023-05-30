#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words and returns a port. """    
    import sys
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    port = 8000
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><head><title>Words</title></head>')
            self.wfile.write(b'<body>')
            self.wfile.write(b'<h1>Words</h1>')
            self.wfile.write(b'<hr>')
            self.wfile.write(b'<p>')
            
            for word in words:
                self.wfile.write(word)
                self.wfile.write('<br>')
            self.wfile.write(b'</p>')
            self.wfile.write(b'</body></html>')
    
    httpd = HTTPServer(('', port), Handler)
    httpd.serve_forever()
    
    sys.exit()
