#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that returns fruits.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(
                "<html><head><title>Fruits</title></head><body>",
                "<h1>Fruits</h1>",
                "<table>",
                "<tr><th>Fruit</th><th>Price</th></tr>",
                "<tr><td>{}</td><td>{}</td></tr>".format(
                    fruir,
                    fruirs[fruirs.index(fruir)]
                )
                for fruir in fruirs
            ))
    
    server = HTTPServer(('', 8000), Handler)
    server.serve_forever()

