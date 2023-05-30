#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write('<html><body>')
            self.wfile.write('<form action="/" method="post">')
            self.wfile.write('<input type="text" name="user">')
            self.wfile.write('<input type="submit" value="Submit">')
            self.wfile.write('</form>')
            self.wfile.write('</body></html>')
    
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    
    print('Starting webserver on port 8080...')
    httpd.serve_forever()
    
