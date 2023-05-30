#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that returns fruits.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(bytes(
                '<html><head><title>Fruits</title></head><body>',
                '<table>',
                '<tr><th>Fruit</th><th>Quantity</th></tr>',
                '<tr><td>%s</td><td>%s</td></tr>' % (
                    fruirs[int(self.path.split('/')[1])],
                    int(self.path.split('/')[2])
                ),
                '</table>',
                '</body></html>',
            ))
    
    server = HTTPServer(('', 8080), ThreadingMixIn(FruitHandler, ))
    server.serve_forever()

