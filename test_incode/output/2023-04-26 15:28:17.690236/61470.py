#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle a GET request """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write('<html><head><title>List of words</title></head>')
            self.wfile.write('<body><p>List of words: </p>')
            self.wfile.write('<ol>\n')
            for word in self.words:
                self.wfile.write('<li>%s</li>\n' % word)
            self.wfile.write('</ol></body></html>')
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Handler)
    
    print('Starting httpd on port 8080')
    httpd.serve_forever()
    
