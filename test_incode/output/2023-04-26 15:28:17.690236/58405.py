#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit(1)
    
    port = sys.argv[1]
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            number = 1
            
            while number < 10:
                number = number + 1
                
                self.wfile.write(str(number))
                
    server = HTTPServer(("", port), MyHandler)
    
    print("Serving at port %s" % port)
    
    server.serve_forever()
    
