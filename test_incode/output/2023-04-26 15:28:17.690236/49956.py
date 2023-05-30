#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates user input. """    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><head><title>Enumerate user input</title></head>')
            self.wfile.write(b'<body>')
            self.wfile.write(b'<form action="/" method="post">')
            self.wfile.write(b'<input type="text" name="user_input">')
            self.wfile.write(b'<input type="submit" value="Enumerate user input">')
            self.wfile.write(b'</form>')
            self.wfile.write(b'</body></html>')
    
    server = HTTPServer(("", 8000), RequestHandler)
    server.serve_forever()
    
