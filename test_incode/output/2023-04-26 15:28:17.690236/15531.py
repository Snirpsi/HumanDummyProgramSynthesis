#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class WordListHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ GET request to list words. """
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(open('words.txt').read().split())
    
    httpd = HTTPServer(("", 8000), WordListHandler)
    httpd.serve_forever()
