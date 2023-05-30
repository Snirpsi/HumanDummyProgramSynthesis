#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python webserver.py <port>")
        sys.exit()
    
    port = int(sys.argv[1])
    
    print("Serving on port %d" % port)
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(b"<html><body>")
            
            html = self.rfile.read()
            
            self.wfile.write(b"<h1>Hello World</h1>")
            self.wfile.write(b"</body></html>")
            
            self.wfile.write(html)
            
    httpd = HTTPServer(("", port), RequestHandler)
    
    print("Serving on port %d" % port)
    httpd.serve_forever()
    
