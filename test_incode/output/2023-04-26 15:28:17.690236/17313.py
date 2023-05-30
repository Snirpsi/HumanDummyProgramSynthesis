#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: %s <port>' % sys.argv[0])
        exit(1)
    
    port = sys.argv[1]
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to a GET request by printing the numbers. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            numbers = [int(x) for x in self.path.split('/')]
            
            for number in numbers:
                print('%d: %s' % (number, number))
    
    httpd = HTTPServer(("", port), Handler)
    
    print('Serving at port %s' % port)
    httpd.serve_forever()

<|/ file filename=server.py |>