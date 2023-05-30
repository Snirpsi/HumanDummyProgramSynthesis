#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write('<html><body>')
            self.wfile.write('<select name="user">')
            for username in ['user1', 'user2', 'user3']:
                self.wfile.write('<option value="%s">%s</option>' % (username, username))
            self.wfile.write('</select>')
            self.wfile.write('</body></html>')
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Handler)
    
    print('Starting server on port 8080')
    httpd.serve_forever()
