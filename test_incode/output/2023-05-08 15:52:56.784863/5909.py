#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that converts a list of words.
    #It also prints the words in reverse order.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(words[::-1]))
    
    server = HTTPServer(('', 8080), Handler)
    ThreadingMixIn.instance().start()
    server.serve_forever()

