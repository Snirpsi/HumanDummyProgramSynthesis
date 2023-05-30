#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port or stores all ports. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class MyHandler(BaseHTTPRequestHandler):
        """ A simple HTTP server that enumerates a port or stores all ports. """
        
        def do_GET(self):
            """ Enumerate all ports """
            
            ports = []
            
            for port in range(0, 65535):
                ports.append(port)
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(str(ports))
            
    httpd = HTTPServer(("", 0), MyHandler)
    httpd.serve_forever()
    
