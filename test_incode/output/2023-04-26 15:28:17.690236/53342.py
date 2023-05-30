#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports. """    
    ports = [8080, 8081, 8082]
    
    httpd = HTTPServer(('', 0), Handler)
    httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='server.key', certfile='server.crt')
    
    for port in ports:
        httpd.serve_forever()
    
    httpd.socket.close()
    httpd.socket.shutdown(socket.SHUT_RDWR)
    httpd.socket.close()
    
    print('Server shut down.')

