#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that calculates fruits.
    #It should serve the fruit list as static content.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    import socketserver

    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = urlparse(self.path).path
            if path == "/":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes("""
                <html>
                <head>
                <title>Fruit list</title>
                </head>
                <body>
                <h1>Fruit list</h1>
                <ul>
                """)
                for fruit in fruirs:
                    self.wfile.write(bytes("""
                    <li>%s</li>
                    """ % fruit))
                self.wfile.write(bytes("""
                </ul>
                </body>
                </html>
                """))
            else:
                self.send_error(404)
                self.end_headers()

    server_address = ('', 8080)
    httpd = HTTPServer(server_address, FruitHandler)
    print('Serving at http://%s:%s/' % (server_address[0], server_address[1]))
    httpd.serve_forever()

