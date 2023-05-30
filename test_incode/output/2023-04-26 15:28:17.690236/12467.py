#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports or stores fruits. """    
    from http.server import BaseHTTPRequestHandler
    import socket
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            ports = []
            
            for port in range(1024):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.bind(('localhost', port))
                sock.listen(1)
                ports.append(port)
                
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            for port in ports:
                sock, addr = sock.accept()
                
                while True:
                    data = sock.recv(1024)
                    if data:
                        self.wfile.write(data)
                    else:
                        break
                
                sock.close()
                
    httpd = BaseHTTPRequestHandler()
    httpd.