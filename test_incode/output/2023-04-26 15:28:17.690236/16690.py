#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports. """    
    from http.server import BaseHTTPRequestHandler
    from urllib.parse import urlparse, parse_qs
    import socketserver
    
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle a GET request """
            parsed_url = urlparse(self.path)
            query = parse_qs(parsed_url.query)
            
            port = int(query['port'][0])
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            self.wfile.write(bytes('<html><body><p>Port <b>%s</b> is <b>%s</b></p></body></html>' % (port, port), 'utf8'))
    
    server_address = ('', 8080)
    httpd = socketserver.TCPServer(server_address, RequestHandler)
    
    httpd.serve_forever()
    
