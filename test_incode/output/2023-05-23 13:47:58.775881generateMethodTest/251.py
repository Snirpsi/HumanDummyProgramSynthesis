#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that adds a list of words.
    import os
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    from urllib.parse import urlparse, parse_qs
    import random
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            query = parse_qs(parsed_url.query)
            
            words = query.get("words", [])
            
            if words:
                words = list(set(words))
                
                random.shuffle(words)
                
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                
                self.wfile.write(" ".join(words))
            else:
                self.send_response(404)
                self.end_headers()
    
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, Handler)
    
    ThreadingMixIn.instance().start()
    
    httpd.serve_forever()
</code>
<|/ a tags=python,python-3.x,webserver |>
<| c |>
Thanks for your answer. Can you please explain what does `self.wfile.write(" ".join(words))` do?
<|/ c |>
<| c |>
`self.wfile` is a `io.BufferedWriter` object which writes its contents to the `self.wfile` file descriptor. `self.wfile.write()` writes the contents of the `words` list to the `self.wfile` file descriptor. `self.wfile.write()` also writes a newline to the `self.wfile` file descriptor which makes the `self.wfile` file descriptor a blocking call. `self.wfile.write()` also writes a newline to the `self.wfile` file descriptor which makes the `self.wfile` file descriptor a blocking call. `self.wfile.write()` also writes a newline to the `self.wfile` file descriptor which makes the `self.wfile` file descriptor a blocking call. `self.wfile.write()` also writes a newline to the `self.wfile` file descriptor which makes the `self.wfile` file descriptor a blocking call. `self.wfile.write()` also writes a newline to the `self.wfile` file descriptor which makes the `self.wfile` file descriptor a blocking call. `self.wfile.write()` also writes a newline to the `self.wfile` file descriptor which makes the `self.wfile` file descriptor a blocking call. `self.wfile.write()` also writes a newline to the `self.wfile` file descriptor which makes the `self.wfile` file descriptor a blocking call. `self.wfile.write()` also writes a newline to the `self.wfile` file descriptor which makes the `self.wfile` file descriptor a blocking call. `self.wfile.write()` also writes a newline to the `self.wfile` file descriptor which makes the `self.wfile` file descriptor a blocking call. `self.wfile.write()` also writes a newline to the `self.wfile` file descriptor which makes the `self.wfile` file descriptor a blocking call. `self.wfile.write()` also writes a newline to the `self.wfile` file descriptor which makes the `self.wfile` file descriptor a blocking call. `self.wfile.write()` also writes a newline to the `self.wfile` file descriptor which makes the `self.wfile` file descriptor a blocking call. `self.wfile.write()` also writes a newline to the `self.wfile` file descriptor which makes the `self.wfile` file descriptor a blocking call. `self.wfile.write()` also writes a newline to the `self.wfile` file descriptor which makes the `self.wfile` file descriptor a blocking call. `self.wfile.write()` also writes a newline to the `self.wfile` file descriptor which makes the `self.wfile` file descriptor a blocking call. `self.wfile.write()` also writes a newline to the `self.wfile` file descriptor which makes the `self.wfile` file descriptor a blocking call. `self.wfile.write()` also writes a newline to the `self.wfile` file descriptor which makes the `self.wfile` file descriptor a blocking call. `self.wfile.write()` also writes a newline to the `self.wfile` file descriptor which makes the `self.wfile` file descriptor a blocking call. `self.wfile.write()` also writes a newline to the `self.wfile` file descriptor which makes the `self.wfile` file descriptor a blocking call. `self.wfile.write()` also writes a newline to the `self.wfile` file descriptor which makes the `self.wfile` file descriptor a blocking call. `self.wfile.write()` also writes a newline to the `self.wfile` file descriptor which makes the `self.wfile` file descriptor a blocking call. `self.wfile.write()` also writes a newline to the `self.wfile` file descriptor which makes the `self.wfile` file descriptor a blocking call. `self.wfile.write()` also writes a newline to the `self.wfile` file descriptor which 