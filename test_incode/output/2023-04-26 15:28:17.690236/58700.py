#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports. """    
    
    ports = [8080, 8081, 8082]
    
    httpd = HTTPServer(('', 0), Handler)
    
    for port in ports:
        httpd.socket = ssl.wrap_socket(httpd.socket, certfile='cert.pem', server_side=True)
        httpd.serve_forever()
        
    httpd.socket.close()
    
