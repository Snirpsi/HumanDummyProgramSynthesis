#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python webserver.py <port>")
        exit(1)
    
    port = int(sys.argv[1])
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle a GET request. """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(bytes("<html><body><h1>Hello World!</h1></body></html>", "utf-8"))
            
    server = HTTPServer(("", port), Handler)
    
    print("Serving on port %d" % port)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.server_close()
    
