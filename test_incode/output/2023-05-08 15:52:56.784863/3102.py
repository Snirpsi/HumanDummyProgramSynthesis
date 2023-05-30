#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that calculates fruits.
    #It only works with python 3.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import os
    import sys
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            #The request is made by the browser
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(
                "<html><head><title>Fruits</title></head>"
                "<body>"
                "<h1>Fruits</h1>"
                "<table>"
                "<tr><th>Fruit</th><th>Count</th></tr>"
                "<tr><td>apple</td><td>1</td></tr>"
                "<tr><td>banana</td><td>2</td></tr>"
                "<tr><td>orange</td><td>3</td></tr>"
                "</table>"
                "</body></html>"
                )
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, FruitHandler)
    print('Starting httpserver on port 8080')
    httpd.serve_forever()

