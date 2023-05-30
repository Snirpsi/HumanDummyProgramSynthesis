#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over user input and prints all ports. """    
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import socket
    
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            """ Handle GET requests. """
            
            # Get port from query string
            port = self.path.split('=')[1]
            
            # Send response to client
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(f'<html><head><title>Port {port}</title></head></html>', 'utf-8'))
            
            # Iterate over all ports
            for port in range(int(port), int(port)+1):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.bind(('localhost', port))
                s.listen(1)
                
                # Handle connection
                conn, addr = s.accept()
                
                # Handle request
                while True:
                    data = conn.recv(1024)
                    
                    # Send response to client
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(bytes(f'<html><head><title>Port {port}</title></head></html>', 'utf-8'))
                    
                    # Send data to client
                    self.wfile.write(bytes(data, 'utf-8'))
                    
                    # Close connection
                    conn.close()
                    
                    # Wait for next request
                    conn.recv(1024)
                    
                # Close socket
                s.close()
                
                # Close connection
                conn.close()
                
                # Close socket
                s.close()
                
                # Wait for next request
                conn.recv(1024)
                
                # Close socket
                s.close()
                
                # Close connection
                conn.close()
                
                # Close socket
                s.close()
                
                # Wait for next request
                conn.recv(1024)
                
                # Close socket
                s.close()
                
                # Close connection
                conn.close()
                
                # Close socket
                s.close()
                
                # Wait for next request
                conn.recv(1024)
                
                # Close socket
                s.close()
                
                # Close connection
                conn.close()
                
                # Close socket
                s.close()
                
                # Wait for next request
                conn.recv(1024)
                
                # Close socket
                s.close()
                
                # Close connection
                conn.close()
                
                # Close socket
                s.close()
                
                # Close connection
                conn.close()
                
                # Close socket
                s.close()
                
                # Close connection
                conn.close()
                
                # Close socket
                s.close()
                
                # Close connection
                conn.