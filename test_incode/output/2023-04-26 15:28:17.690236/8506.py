#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits. """    
    
    import sys
    
    port = sys.argv[1]
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            path = urllib.parse.urlparse(self.path).path
            
            if path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write('<html><body>')
                self.wfile.write('<h1>Fruits</h1>')
                self.wfile.write('<ul>')
                
                for fruit in ['apple', 'orange', 'pear']:
                    self.wfile.write('<li><a href="/fruit/%s">%s</a></li>' % (fruit, fruit))
                
                self.wfile.write('</ul></body></html>')
                
            else:
                self.send_error(404)
                
    httpd = HTTPServer(("", port), FruitHandler)
    
    print("Serving at port %s" % port)
    
    httpd.serve_forever()
    
