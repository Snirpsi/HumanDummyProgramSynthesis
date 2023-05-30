#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs
    from urllib.parse import urlparse
    
    class RequestHandler(BaseHTTPRequestHandler):
        """ A simple request handler that converts numbers. """
        
        def do_GET(self):
            """ Handle a GET request. """
            
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                """ Handle a GET request to /. """
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<h1>Convert numbers</h1>')
                self.wfile.write(b'<form action="/convert" method="GET"><input type="text" name="num1" value="0"><input type="text" name="num2" value="0"><input type="submit" value="Convert"><input type="reset" value="Reset"></form>')
                self.wfile.write(b'</body></html>')
                
            elif parsed_url.path == '/convert':
                """ Handle a GET request to /convert. """
                
                num1 = int(parse_qs(parsed_url.query)['num1'][0])
                num2 = int(parse_qs(parsed_url.query)['num2'][0])
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<h1>Convert numbers</h1>')
                self.wfile.write(b'<form action="/convert" method="GET"><input type="text" name="num1" value="%d"><input type="text" name="num2" value="%d"><input type="submit" value="Convert"><input type="reset" value="Reset"></form>' % num1, num2)
                self.wfile.write(b'</body></html>')
                
            elif parsed_url.path == '/reset':
                """ Handle a GET request to /reset. """
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<h1>Reset numbers</h1>')
                self.wfile.write(b'<form action="/reset" method="GET"><input type="submit" value="Reset"></form>')
                self.wfile.write(b'</body></html>')
                
            else:
                """ Handle a GET request to /something. """
                
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<h1>Something went wrong</h1>')
                self.wfile.write(b'</body></html>')
                
    httpd = HTTPServer(('', 8080), RequestHandler)
    
    httpd.serve_forever()
