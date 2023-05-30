#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words or opens numbers. """    
    from http.server import BaseHTTPRequestHandler
    from urllib.parse import urlparse
    import socket
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Returns words or numbers. """
            parsed_url = urlparse(self.path)
            
            if parsed_url.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                self.wfile.write(b'<html><body>')
                self.wfile.write(b'<center><h1>')
                self.wfile.write(b'Opening numbers...')
                self.wfile.write(b'</h1></center>')
                self.wfile.write(b'</body></html>')
            else:
                
                parsed_url = urlparse(parsed_url.path)
                
                if parsed_url.path == '/numbers':
                    
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    
                    self.wfile.write(b'<html><body>')
                    self.wfile.write(b'<center><h1>')
                    self.wfile.write(b'Opening numbers...')
                    self.wfile.write(b'</h1></center>')
                    self.wfile.write(b'</body></html>')
                    
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.bind(('localhost', 8080))
                    s.listen(1)
                    
                    while True:
                        
                        conn, addr = s.accept()
                        
                        while True:
                            
                            data = conn.recv(1024)
                            
                            if not data:
                                break
                            
                            conn.sendall(data)
                            
                            data = conn.recv(1024)
                            
                            if not data:
                                break
                            
                            conn.sendall(data)
                            
                            data = conn.recv(1024)
                            
                            if not data:
                                break
                            
                            conn.sendall(data)
                            
                            data = conn.recv(1024)
                            
                            if not data:
                                break
                            
                            conn.sendall(data)
                            
                            data = conn.recv(1024)
                            
                            if not data:
                                break
                            
                            conn.sendall(data)
                            
                            data = conn.recv(1024)
                            
                            if not data:
                                break
                            
                            conn.sendall(data)
                            
                            data = conn.recv(1024)
                            
                            if not data:
                                break
                            
                            conn.sendall(data)
                            
                            data = conn.recv(1024)
                            
                            if not data:
                                break
                            
                            conn.sendall(data)
                            
                            data = conn.recv(1024)
                            
                            if not data:
                                break
                            
                            conn.sendall(data)
                            
                            data = conn.recv(1024)
                            
                            if not data:
                                break