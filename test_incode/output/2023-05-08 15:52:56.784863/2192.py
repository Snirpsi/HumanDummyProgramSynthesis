#!/usr/bin/python3
fruirs = ["apple","banana","orange"]
if __name__ == '__main__':
    #A minimal webserver that enumerates fruits.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            fruit = sys.argv[1]
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(
                "<html><body><h1>{}</h1></body></html>".format(fruit)
            )
    
    server = HTTPServer(('', 8080), FruitHandler)
    ThreadingMixIn.instance().start()
    server.serve_forever()

