#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input and returns a list of words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    import json
    import random
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to GET requests. """
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<h1>Enumerate Words</h1>')
                self.wfile.write(b'<form action="/" method="post">')
                self.wfile.write(b'<input type="text" name="word">')
                self.wfile.write(b'<input type="submit" value="Enumerate">')
                self.wfile.write(b'</form>')
                self.wfile.write(b'</body></html>')
                return
            
            words = json.loads(request.get_data(as_text=True))
            
            random.shuffle(words)
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body>')
            self.wfile.write(b'<h1>Enumerate Words</h1>')
            self.wfile.write(b'<form action="/" method="post">')
            self.wfile.write(b'<input type="text" name="word">')
            self.wfile.write(b'<input type="submit" value="Enumerate">')
            self.wfile.write(b'</form>')
            self.wfile.write(b'</body></html>')
            
            for word in words:
                self.wfile.write(b'<p>%s</p>' % word)
            
            self.wfile.write(b'</body></html>')
            
    server = HTTPServer(('', 8080), Handler)
    server.serve_forever()

<|/ file filename=server.py |>