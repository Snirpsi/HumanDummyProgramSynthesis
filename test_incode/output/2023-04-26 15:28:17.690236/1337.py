#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input and returns words. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body>')
            self.wfile.write(b'<form action="/" method="POST">')
            self.wfile.write(b'<input type="text" name="word">')
            self.wfile.write(b'<input type="submit" value="Submit">')
            self.wfile.write(b'</form>')
            self.wfile.write(b'</body></html>')
    
    server = HTTPServer(('', 8080), RequestHandler)
    server.serve_forever()
    
