#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that returns user input.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes('<html><body>', 'utf-8'))
            self.wfile.write(bytes('<form action="/" method="post"><input type="text" name="user"><input type="submit" value="Submit"></form>', 'utf-8'))
            self.wfile.write(bytes('</body></html>', 'utf-8'))
    
    httpd = HTTPServer(('localhost', 8080), Handler)
    
    print('Serving on port 8080')
    httpd.serve_forever()

