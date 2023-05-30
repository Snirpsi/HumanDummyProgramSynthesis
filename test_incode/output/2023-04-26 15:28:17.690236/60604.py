#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                """ Root path request. """
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write('<html><body>')
                self.wfile.write('<form action="/" method="post">')
                self.wfile.write('<input type="text" name="user">')
                self.wfile.write('<input type="submit" value="Submit">')
                self.wfile.write('</form>')
                self.wfile.write('</body></html>')
                return
            
            if parsed_url.path == '/user':
                """ User path request. """
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write('<html><body>')
                self.wfile.write('<h1>User input</h1>')
                self.wfile.write('<form action="/user" method="post">')
                self.wfile.write('<input type="text" name="user">')
                self.wfile.write('<input type="submit" value="Submit">')
                self.wfile.write('</form>')
                self.wfile.write('</body></html>')
                return
            
            self.send_error(404)
    
    httpd = HTTPServer(('', 8080), RequestHandler)
    