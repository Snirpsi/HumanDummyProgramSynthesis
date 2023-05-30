#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port and iterates over all ports. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        """ A simple HTTP server that opens a port and iterates over all ports. """
        
        def do_GET(self):
            """ Handle a GET request. """
            
            port = self.server.server_port
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(f'<html><head><title>{port}</title></head><body>')
            self.wfile.write(f'<p> Port {port} is open. </p>')
            self.wfile.write(f'</body></html>')
            
            self.wfile.flush()
            
    httpd = HTTPServer(("", 8080), Handler)
    
    print(f'Serving on port {httpd.server_port}')
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        
    print('\nExiting...')
    
