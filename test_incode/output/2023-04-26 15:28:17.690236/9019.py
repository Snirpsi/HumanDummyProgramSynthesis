#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports. """    
    ports = [8000, 8001, 8002]
    
    httpd = HTTPServer(('', 0), Handler)
    
    for port in ports:
        httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='./key.pem', certfile='./cert.pem', server_side=True)
        httpd.serve_forever()
        
    httpd.socket.close()
    httpd.server_close()
    
