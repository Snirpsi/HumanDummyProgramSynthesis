#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit(1)
    
    port = int(sys.argv[1])
    
    print("Serving on port %d" % port)
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to a GET request by printing the numbers. """
            numbers = []
            for i in range(10):
                numbers.append(i)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(str(numbers))
    
    httpd = HTTPServer(('', port), MyHandler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    
    httpd.server_close()

<|/ file filename=server.py source=github |>