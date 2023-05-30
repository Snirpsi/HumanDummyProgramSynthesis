#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes user input. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    
    class RequestHandler(BaseHTTPRequestHandler):
        """ A request handler that multiplies user input. """
        def do_GET(self):
            """ Handle a GET request. """
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                """ Handle a GET request to /. """
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<form action="/" method="POST">')
                self.wfile.write(b'<input type="text" name="num1" value="0">')
                self.wfile.write(b'<input type="text" name="num2" value="0">')
                self.wfile.write(b'<input type="submit" value="Submit">')
                self.wfile.write(b'</form>')
                self.wfile.write(b'</body></html>')
            elif parsed_url.path == '/multiply':
                """ Handle a GET request to /multiply. """
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<form action="/" method="POST">')
                self.wfile.write(b'<input type="text" name="num1" value="0">')
                self.wfile.write(b'<input type="text" name="num2" value="0">')
                self.wfile.write(b'<input type="submit" value="Submit">')
                self.wfile.write(b'</form>')
                self.wfile.write(b'</body></html>')
            elif parsed_url.path == '/multiply?num1=2&num2=3':
                """ Handle a GET request to /multiply?num1=2&num2=3. """
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<form action="/" method="POST">')
                self.wfile.write(b'<input type="text" name="num1" value="0">')
                self.wfile.write(b'<input type="text" name="num2" value="0">')
                self.wfile.write(b'<input type="submit" value="Submit">')
                self.wfile.write(b'</form>')
                self.wfile.write(b'</body></html>')
            else:
                """ Handle a GET request to /multiply?num1=2&num2=3. """
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<h1>Not found</h1>')
                self.wfile.write(b'</body></html>')
        
    httpd = HTTPServer(('', 8080), RequestHandler)
    httpd.serve_forever()
