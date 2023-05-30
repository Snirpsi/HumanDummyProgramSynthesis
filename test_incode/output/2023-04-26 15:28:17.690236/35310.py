#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            query = self.path.split('?')[1]
            
            if query:
                query = query.split('&')
                
                for item in query:
                    key, value = item.split('=')
                    
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    
                    self.wfile.write(bytes(f'<html><head><title>{key}</title></head><body>{value}</body></html>', 'utf-8'))
                    
            else:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(bytes(f'<html><head><title>{key}</title></head><body>{value}</body></html>', 'utf-8'))
                
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    
    print('Serving on port 8080')
    
    httpd.serve_forever()
    
