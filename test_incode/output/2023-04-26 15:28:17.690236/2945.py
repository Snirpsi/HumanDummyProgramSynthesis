#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class WebServer(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to GET requests. """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            ports = enumerate()
            
            for port in ports:
                self.wfile.write(bytes(f'<html><head><title>{port}</title></head><body><p>Port {port}</p></body></html>', 'utf-8'))
            
    httpd = HTTPServer(("", 80), WebServer)
    
    httpd.serve_forever()
    
