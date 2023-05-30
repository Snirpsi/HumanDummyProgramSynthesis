#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports or removes fruits. """    
    from http.server import BaseHTTPRequestHandler
    from urllib.parse import urlparse, parse_qs
    import socketserver
    
    class FruitHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to GET requests. """
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/fruit':
                """ Respond to GET requests with list of fruits. """
                fruits = ['apple', 'banana', 'cherry']
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(fruits)
            elif parsed_url.path == '/fruit/remove':
                """ Respond to GET requests with list of fruits. """
                fruits = ['apple', 'banana', 'cherry']
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(fruits)
            else:
                """ Respond to GET requests with 404 error. """
                self.send_response(404)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write('404 Not Found')
    
    server_address = ('', 8080)
    httpd = socketserver.TCPServer(server_address, FruitHandler)
    httpd.serve_forever()
