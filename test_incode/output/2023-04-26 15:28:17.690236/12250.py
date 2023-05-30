#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    print("Serving on port %d" % port)
    
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    
    class MyHandler(SimpleHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            """ Get a GET request and parse it into a number. """
            
            """ Send the number back to the client. """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(str(int(sys.argv[2])))
    
    httpd = HTTPServer(('', port), MyHandler)
    
    print("Serving on port %d" % port)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    
    httpd.server_close()
    
    print("Done.")

<|/ file source=github filename=