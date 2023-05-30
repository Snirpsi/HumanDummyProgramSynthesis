#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that returns fruits.
    #It will listen on port 8080 and will return the fruits it finds.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            #The request is made to the server and is processed.
            #The server will respond with a 200 OK response.
            #The response will contain the fruits it finds.
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(
                '<html><body><h1>Fruits</h1></body></html>',
                'utf-8'))
    
    server = HTTPServer(('localhost', 8080), FruitHandler)
    server.serve_forever()

