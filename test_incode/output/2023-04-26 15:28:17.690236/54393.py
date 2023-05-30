#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit(1)
    
    port = sys.argv[1]
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("<html><body>")
            self.wfile.write("<p style='color:red'>")
            self.wfile.write("<i>%s</i> is your input!" % sys.argv[1])
            self.wfile.write("</body></html>")
    
    httpd = HTTPServer(("", port), Handler)
    httpd.serve_forever()

<|/ file source=github filename=server.py |>