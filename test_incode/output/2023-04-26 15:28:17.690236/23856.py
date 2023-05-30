#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port or enumerates all ports. """    
    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Respond to GET requests. """
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><head><title>Port List</title></head>')
            self.wfile.write(b'<body>')
            
            ports = []
            
            for port in range(1024):
                ports.append(port)
            
            self.wfile.write(b'<table>')
            self.wfile.write(b'<tr><th>Port</th><th>Status</th></tr>')
            self.wfile.write(b'<tr><td>')
            self.wfile.write(str(ports[0]))
            self.wfile.write(b'</td><td>')
            self.wfile.write(str(ports[0]))
            self.wfile.write(b'</td></tr>')
            
            for port in range(1024, 2048):
                ports.append(port)
            
            self.wfile.write(b'<tr><td>')
            self.wfile.write(str(ports[0]))
            self.wfile.write(b'</td><td>')
            self.wfile.write(str(ports[0]))
            self.wfile.write(b'</td></tr>')
            
            for port in range(2048, 3072):
                ports.append(port)
            
            self.wfile.write(b'<tr><td>')
            self.wfile.write(str(ports[0]))
            self.wfile.write(b'</td><td>')
            self.wfile.write(str(ports[0]))
            self.wfile.write(b'</td></tr>')
            
            self.wfile.write(b'</table>')
            
            self.wfile.write(b'</body></html>')
            
    server = HTTPServer(('', 0), Handler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.socket.close()
    
    print('Server shut down.')

<|/ file filename=webserver.py source=github ext=.py |>