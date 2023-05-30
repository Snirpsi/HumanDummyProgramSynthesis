#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <port>' % sys.argv[0])
        sys.exit(1)
    
    port = int(sys.argv[1])
    
    from http.server import BaseHTTPRequestHandler
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body>')
            self.wfile.write(b'<h1>User input</h1>')
            self.wfile.write(b'<form action="/" method="post">')
            self.wfile.write(b'<input type="text" name="user">')
            self.wfile.write(b'<input type="submit" value="Submit">')
            self.wfile.write(b'</form>')
            self.wfile.write(b'</body></html>')
    
    server_address = ('', port)
    httpd = BaseHTTPRequestHandler
    httpd.