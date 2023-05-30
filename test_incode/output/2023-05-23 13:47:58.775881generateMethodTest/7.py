#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that requests user input.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from socketserver import ThreadingMixIn
    from socketserver import StreamRequestHandler
    from io import BytesIO

    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_url = urlparse(self.path)
            if parsed_url.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<form action="/" method="post">')
                self.wfile.write(b'<input type="text" name="user">')
                self.wfile.write(b'<input type="submit" value="Submit">')
                self.wfile.write(b'</form>')
                self.wfile.write(b'</body></html>')
            elif parsed_url.path == '/user':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<form action="/" method="post">')
                self.wfile.write(b'<input type="text" name="user">')
                self.wfile.write(b'<input type="submit" value="Submit">')
                self.wfile.write(b'</form>')
                self.wfile.write(b'</body></html>')
            elif parsed_url.path == '/users':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<form action="/" method="post">')
                self.wfile.write(b'<input type="text" name="user">')
                self.wfile.write(b'<input type="submit" value="Submit">')
                self.wfile.write(b'</form>')
                self.wfile.write(b'</body></html>')
            elif parsed_url.path == '/user/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<form action="/" method="post">')
                self.wfile.write(b'<input type="text" name="user">')
                self.wfile.write(b'<input type="submit" value="Submit">')
                self.wfile.write(b'</form>')
                self.wfile.write(b'</body></html>')
            elif parsed_url.path == '/user/1':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<form action="/" method="post">')
                self.wfile.write(b'<input type="text" name="user">')
                self.wfile.write(b'<input type="submit" value="Submit">')
                self.wfile.write(b'</form>')
                self.wfile.write(b'</body></html>')
            elif parsed_url.path == '/user/1/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<form action="/" method="post">')
                self.wfile.write(b'<input type="text" name="user">')
                self.wfile.write(b'<input type="submit" value="Submit">')
                self.wfile.write(b'</form>')
                self.wfile.write(b'</body></html>')
            elif parsed_url.path == '/user/1/1':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<form action="/" method="post">')
                self.wfile.write(b'<input type="text" name="user">')
                self.wfile.write(b'<input type="submit" value="Submit">')
                self.wfile.write(b'</form>')
                self.wfile.write(b'</body></html>')
            elif parsed_url.path == '/user/1/1/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<form action="/" method="post">')
                self.wfile.write(b'<input type="text" name="user">')
                self.wfile.write(b'<input type="submit" value="Submit">')
                self.wfile.write(b'</form>')
                self.wfile.write(b'</body></html>')
            elif parsed_url.path == '/user/1/1/1':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<form action="/" method="post">')
                self.wfile.write(b'<input type="text" name="user">')
                self.wfile.write(b'<input type="submit" value="Submit">')
                self.wfile.write(b'</form>')
                self.wfile.write(b'</body></html>')
            elif parsed_url.path == '/user/1/1/1/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<form action="/" method="post">')
                self.wfile.write(b'<input type="text" name="user">')
                self.wfile.write(b'<input type="submit" value="Submit">')
                self.wfile.write(b'</form>')
                self.wfile.write(b'</body></html>')
            elif parsed_url.path == '/user/1/1/1/1':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<form action="/" method="post">')
                self.wfile.write(b'<input type="text" name="user">')
                self.wfile.write(b'<input type="submit" value="Submit">')
                self.wfile.write(b'</form>')
                self.wfile.write(b'</body></html>')
            elif parsed_url.path == '/user/1/1/1/1/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_