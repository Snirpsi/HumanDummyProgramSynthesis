#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to a GET request by printing all words. """
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            self.wfile.write(b'\n'.join(words for words in words))
    
    httpd = HTTPServer(("", 80), MyHandler)
    httpd.serve_forever()
    
