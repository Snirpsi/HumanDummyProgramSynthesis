#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input. """    
    import sys
    import socketserver
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            query = parse_qs(urlparse(self.path).query)
            
            host = query['host'][0]
            port = query['port'][0]
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(self.server.server_address[0] + ':' + str(port) + '\n')
            
            self.wfile.write(self.server.server_address[0] + ':' + str(port) + '\n')
            
            self.wfile.write(self.server.server_address[0] + ':' + str(port) + '\n')
            
            self.wfile.write(self.server.server_address[0] + ':' + str(port) + '\n')
            
            self.wfile.write(self.server.server_address[0] + ':' + str(port) + '\n')
            
            self.wfile.write(self.server.server_address[0] + ':' + str(port) + '\n')
            
            self.wfile.write(self.server.server_address[0] + ':' + str(port) + '\n')
            
            self.wfile.write(self.server.server_address[0] + ':' + str(port) + '\n')
            
            self.wfile.write(self.server.server_address[0] + ':' + str(port) + '\n')
            
            self.wfile.write(self.server.server_address[0] + ':' + str(port) + '\n')
            
            self.wfile.write(self.server.server_address[0] + ':' + str(port) + '\n')
            
            self.wfile.write(self.server.server_address[0] + ':' + str(port) + '\n')
            
            self.wfile.write(self.server.server_address[0] + ':' + str(port) + '\n')
            
            self.wfile.write(self.server.server_address[0] + ':' + str(port) + '\n')
            
            self.wfile.write(self.server.server_address[0] + ':' + str(port) + '\n')
            
            self.wfile.write(self.server.server_address[0] + ':' + str(port) + '\n')
            
            self.wfile.write(self.server.server_address[0] + ':' + str(port) + '\n')
            
            self.wfile.write(self.server.server_address[0] + ':' + str(port) + '\n')
            
            self.wfile.write(self.server.server_address[0] + ':' + str(port) + '\n')
            
            self.wfile.write(self.server.server_address[0] + ':' + str(port) + '\n')
            
            self.wfile.write(self.server.server_address[0] + ':' + str(port) + '\n')
            
            self.wfile.write(self.server.server_address[0] + ':' + str(port) + '\n')
            
            self.wfile.write(self.server.server_address[0] + ':' + str(port) + '\n')
            
            self.w