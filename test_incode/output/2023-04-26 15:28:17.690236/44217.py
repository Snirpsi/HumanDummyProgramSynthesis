#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers or stores numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("usage: python webserver.py <port>")
        sys.exit()
    
    port = int(sys.argv[1])
    
    print("Starting webserver on port %d" % port)
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><head><title>Enumerate numbers</title></head>')
            self.wfile.write(b'<body>')
            self.wfile.write(b'<table>')
            
            numbers = []
            
            for num in range(1, 10):
                numbers.append(num)
                
                self.wfile.write(b'<tr><td>%d</td><td>%s</td></tr>' % (num, str(num)))
                
            self.wfile.write(b'</table></body></html>')
            
    httpd = HTTPServer(('', port), Handler)
    
    print("Serving webserver on port %d" % port)
    
    httpd.serve_forever()
    
