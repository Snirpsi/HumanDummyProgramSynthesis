#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers and prints a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    print("Serving on port %s" % port)
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            numbers = range(10)
            
            self.wfile.write(
                '<html><body>'
                '<table>'
                '<tr><th>Number</th><th>Word</th></tr>'
                '<tr><td>%d</td><td>%s</td></tr>'
                '</table>'
                '</body></html>'
                % (numbers[0], numbers[0]))
            
    httpd = HTTPServer(("", port), Handler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
    
