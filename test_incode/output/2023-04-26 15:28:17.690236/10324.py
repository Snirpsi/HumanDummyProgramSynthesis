#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class MyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><head><title>User input</title></head>')
            self.wfile.write(b'<body>')
            self.wfile.write(b'<form action="/" method="POST">')
            self.wfile.write(b'<input type="text" name="user"><br>')
            self.wfile.write(b'<input type="submit" value="Submit">')
            self.wfile.write(b'</form>')
            self.wfile.write(b'</body></html>')
    
    server = HTTPServer(('', 8080), MyHandler)
    server.serve_forever()
    
