#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words. """    
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    from urllib.parse import urlparse
    
    server_address = ('localhost', 8000)
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(b'<html><head><title>Words</title></head>')
                self.wfile.write(b'<body>')
                self.wfile.write(b'<h1>Words</h1>')
                self.wfile.write(b'</body></html>')
            else:
                self.send_error(404)
    
    httpd = HTTPServer(server_address, RequestHandler)
    
    httpd.serve_forever()
    
