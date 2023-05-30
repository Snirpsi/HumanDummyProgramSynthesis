#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            number = self.path.split('/')[-1]
            
            number = int(number)
            
            html = "<html><body><p>The number is: %s</p></body></html>" % number
            
            self.wfile.write(html)
    
    server = HTTPServer(("", port), MyHandler)
    
    print("Serving on port %s..." % port)
    
    server.serve_forever()
    
