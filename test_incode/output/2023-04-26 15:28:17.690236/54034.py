#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports and enumerates fruits. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><head><title>Fruitlist</title></head>')
            self.wfile.write(b'<body>')
            self.wfile.write(b'<h1>Fruitlist</h1>')
            self.wfile.write(b'<hr>')
            self.wfile.write(b'<table>')
            for fruit in Fruits.fruits:
                self.wfile.write(b'<tr><td>')
                self.wfile.write(str(fruit))
                self.wfile.write(b'</td><td>')
                self.wfile.write(str(Fruits.fruits.count(fruit)))
                self.wfile.write(b'</td></tr>')
            self.wfile.write(b'</table>')
            self.wfile.write(b'</body></html>')
    
    server = HTTPServer(('', PORT), FruitHandler)
    server.serve_forever()
    
