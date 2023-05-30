#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(b'<html><head><title>User Input</title></head>')
            self.wfile.write(b'<body>')
            
            html = ''
            
            for line in self.rfile.readlines():
                html += line
                
            self.wfile.write(b'<p>%s</p>' % html)
            self.wfile.write(b'</body></html>')
            
    server = HTTPServer(('', 8080), RequestHandler)
    
    print('Serving on port 8080')
    server.serve_forever()
