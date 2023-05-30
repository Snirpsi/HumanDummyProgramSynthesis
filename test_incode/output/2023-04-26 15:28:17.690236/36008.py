#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports or opens words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Serve the requested file from the current directory """
            path = os.path.abspath(self.path)
            
            if path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(self.server.index_html)
            else:
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(open(path).read())
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    
    print('Serving at http://%s:%s/' % (server_address[0], server_address[1]))
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    
    httpd.server_close()

<|/ file ext=.py source=github |>