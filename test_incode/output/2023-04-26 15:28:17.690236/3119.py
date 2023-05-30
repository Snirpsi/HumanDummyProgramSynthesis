#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class WebServer(BaseHTTPRequestHandler):
        
        def do_GET(self):
            """ Handle GET requests. """
            
            port = self.server.server_port
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(f'<html><head><title>WebServer on port {port}</title></head><body>')
            self.wfile.write(f'<h1>WebServer on port {port}</h1>')
            self.wfile.write(f'<p><a href="http://localhost:{port}/">Click here</a> to view the web page</p>')
            self.wfile.write(f'</body></html>')
            
    httpd = HTTPServer(("", 8080), WebServer)
    
    httpd.serve_forever()
    
