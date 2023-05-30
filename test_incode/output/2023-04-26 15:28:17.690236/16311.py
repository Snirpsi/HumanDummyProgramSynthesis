#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits or iterates over words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("usage: python server.py [port]")
        sys.exit(0)
    
    port = int(sys.argv[1])
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/':
                response = '<html><head><title>Fruits</title></head>'
                response += '<body><h1>Fruits</h1>'
                response += '<ul>'
                for fruit in Fruit:
                    response += '<li>' + fruit + '</li>'
                response += '</ul></body></html>'
                self.send_response(200)
                self.end_headers()
                self.wfile.write(response.encode())
            else:
                response = '<h1>' + Fruit[self.path.split('/')[1]] + ' not found</h1>'
                self.send_response(404)
                self.end_headers()
                self.wfile.write(response.encode())
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, Handler)
    
    print("Serving at port", port)
    httpd.serve_forever()
    
