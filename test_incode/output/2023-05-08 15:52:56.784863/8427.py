#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that enumerates fruits.
    #This example is intended to be run as a standalone script.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(
                '<html><head><title>Fruits</title></head>'
                '<body>'
                '<h1>Fruits</h1>'
                '<table>'
                '<tr><th>Fruit</th><th>Count</th></tr>'
                '<tr><td>apple</td><td>1</td></tr>'
                '<tr><td>banana</td><td>2</td></tr>'
                '<tr><td>orange</td><td>3</td></tr>'
                '</table>'
                '</body></html>'
                )
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, FruitHandler)
    ThreadingMixIn.instance().start()
    httpd.serve_forever()

