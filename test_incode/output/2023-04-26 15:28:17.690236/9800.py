#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words and enumerates a port. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from socketserver import ThreadingMixIn
    
    class WordsHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(bytes('<html><body>', 'utf-8'))
            self.wfile.write(bytes('<H1>Words</H1>', 'utf-8'))
            self.wfile.write(bytes('<H2>Enumerate port</H2>', 'utf-8'))
            self.wfile.write(bytes('<H3>http://localhost:<PORT></H3>', 'utf-8'))
            self.wfile.write(bytes('</body></html>', 'utf-8'))
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, WordsHandler)
    ThreadingMixIn.instance().