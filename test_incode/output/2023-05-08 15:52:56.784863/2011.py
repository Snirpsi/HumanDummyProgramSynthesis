#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that removes a list of words.
    #It also prints out the words that have been removed.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(words, "utf-8"))
    
    server = HTTPServer(('localhost', 8000), Handler)
    server.serve_forever()

