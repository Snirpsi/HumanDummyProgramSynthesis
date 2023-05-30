#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit(1)
    
    port = int(sys.argv[1])
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            content = str(self.request.recv(1024), 'utf-8')
            
            try: 
                number = int(content)
            except ValueError:
                number = content
                
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(str(number))
            
    server = HTTPServer(("", port), MyHandler)
    
    print("Serving on port %s" % port)
    server.serve_forever()
    
