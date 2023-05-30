#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input. """    
    from http.server import BaseHTTPRequestHandler
    from urllib.parse import urlparse
    import socket
    
    class RequestHandler(BaseHTTPRequestHandler):
        """ A simple request handler that prints user input. """
        def do_GET(self):
            """ Handle a GET request. """
            parsed_url = urlparse(self.path)
            if parsed_url.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<form action="/" method="GET"><input type="text" name="input"><input type="submit" value="Submit"></form></body></html>')
            else:
                self.send_error(404)
    
    server_address = ('', 8080)
    httpd = BaseHTTPRequestHandler.HTTPServer(server_address, RequestHandler)
    