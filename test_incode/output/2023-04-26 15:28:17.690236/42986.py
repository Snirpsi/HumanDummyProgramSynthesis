#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit(1)
    
    port = int(sys.argv[1])
    
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    
    class Handler(SimpleHTTPRequestHandler):
        def do_GET(self):
            """ GET request handler. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write("<html><body><h1>Hello World!</h1></body></html>")
    
    httpd = 