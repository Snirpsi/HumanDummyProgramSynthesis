#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    
    from http.server import BaseHTTPRequestHandler
    from urllib.parse import urlparse
    import socketserver
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to a GET request by listing all words. """
            
            path = urlparse(self.path).path
            
            if path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><head><title>Words</title></head>')
                self.wfile.write(b'<body>')
                self.wfile.write(b'<h1>Words</h1>')
                self.wfile.write(b'<table>')
                self.wfile.write(b'<tr><th>Word</th><th>Count</th></tr>')
                
                words = []
                
                for word in words:
                    self.wfile.write(b'<tr><td>{}</td><td>{}</td></tr>'.format(word, len(words)))
                
                self.wfile.write(b'</table></body></html>')
                
            else:
                words = open(path).read().splitlines()
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><head><title>Words</title></head>')
                self.wfile.write(b'<body>')
                self.wfile.write(b'<h1>Words</h1>')
                self.wfile.write(b'<table>')
                self.wfile.write(b'<tr><th>Word</th><th>Count</th></tr>')
                
                for word in words:
                    self.wfile.write(b'<tr><td>{}</td><td>{}</td></tr>'.format(word, len(words)))
                
                self.wfile.write(b'</table></body></html>')
                
    httpd = socketserver.TCPServer(("", 8080), Handler)
    httpd.serve_forever()
    
