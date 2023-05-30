#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('usage: python -m SimpleHTTPServer port')
        sys.exit(1)
    
    port = sys.argv[1]
    
    print('Serving HTTP on port ' + str(port) + '...')
    
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    
    class MyRequestHandler(SimpleHTTPRequestHandler):
        def do_GET(self):
            """ Handle a GET request """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body>')
            self.wfile.write(b'<h1>Hello, world!</h1>')
            self.wfile.write(b'</body></html>')
    
    httpd = HTTPServer(('', port), MyRequestHandler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    
    print('Stopping server...')
    
    httpd.server_close()
    
    print('Done.')

<|/ file filename=SimpleHTTPServer.py |>