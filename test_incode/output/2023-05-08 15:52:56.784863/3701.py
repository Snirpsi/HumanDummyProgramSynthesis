#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that converts a list of words.
    #It also prints the words in reverse order.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    import sys
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == "/":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(bytes("".join(reversed(words)), "utf8"))
            else:
                self.send_error(404)
    
    server = HTTPServer(('', 8000), Handler)
    server.serve_forever()

