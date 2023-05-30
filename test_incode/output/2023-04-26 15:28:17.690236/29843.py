#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python -m webserver [port]')
        sys.exit()
    
    port = int(sys.argv[1])
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Convert numbers to strings. """
            
            number = self.path.split('/')[-1]
            
            number = '0' if number[0] == '0' else number
            
            number = int(number)
            
            number = str(number)
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(number)
    
    httpd = HTTPServer(("", port), Handler)
    
    print("Serving at port %d" % port)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    
    httpd.server_close()

<|/ file ext=.py source=github filename=webserver.py |>