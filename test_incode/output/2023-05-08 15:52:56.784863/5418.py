#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that returns fruits.
    #It can be run from the command line or with python -m http.server
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(
                "<html><body>"
                "<table>"
                "<tr><th>Fruit</th><th>Price</th></tr>"
                "<tr><td>{}</td><td>{}</td></tr>"
                "</table>"
                "</body></html>".format(fruirs, self.get_argument('price'))
            )
    
    server = HTTPServer(('', 8080), Handler)
    server.serve_forever()

