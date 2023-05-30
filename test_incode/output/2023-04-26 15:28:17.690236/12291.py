#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse, parse_qs
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<form action="/" method="post">')
                self.wfile.write(b'<input name="user" type="text">')
                self.wfile.write(b'<input name="submit" type="submit" value="Submit">')
                self.wfile.write(b'</form>')
                self.wfile.write(b'</body></html>')
                return
            
            parsed_query = parse_qs(parsed_url.query)
            
            if 'user' in parsed_query:
                user = parsed_query['user'][0]
            else:
                user = 'Guest'
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body>')
            self.wfile.write(b'<form action="/" method="post">')
            self.wfile.write(b'<input name="user" type="text" value="%s">' % user)
            self.wfile.write(b'<input name="submit" type="submit" value="Submit">')
            self.wfile.write(b'</form>')
            self.wfile.write(b'</body></html>')
    
    httpd = HTTPServer(('', 8000), Handler)
    httpd.serve_forever()