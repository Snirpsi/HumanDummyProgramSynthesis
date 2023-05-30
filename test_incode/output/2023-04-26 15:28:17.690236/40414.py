#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words and enumerates a port. """    
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    from socketserver import ThreadingMixIn
    from time import sleep

    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            path = self.path
            if path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<h1>Hello World!</h1>')
                self.wfile.write(b'</body></html>')
            elif path == '/enumerate':
                port = int(sys.argv[1])
                ports = [port]
                sleep(1)
                for port in ports:
                    ports.append(port + 1)
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<h1>Enumerating ports {0}</h1>'.format(ports))
                self.wfile.write(b'</body></html>')
            else:
                self.send_error(404)

    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    ThreadingMixIn.instance().