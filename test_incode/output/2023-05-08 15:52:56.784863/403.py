#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that requests a list of words.
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from socketserver import ThreadingMixIn
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsedUrl = urlparse(self.path)
            words = parsedUrl.path.split('/')
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(bytes(
                '<html><head><title>Words list</title></head>'
                '<body><p>Words list</p>'
                '<ul>'
                '<li>%s</li>'
                '</ul></body></html>'
                % '\n'.join(words)
            ))
    
    server = HTTPServer(('', 8080), Handler)
    ThreadingMixIn.instance().start()
    
    server.serve_forever()

