#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that stores a list of words.
    #The server will listen for connections and serve the requested page
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(words, "utf8"))
    
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, Handler)
    
    httpd.serve_forever()

