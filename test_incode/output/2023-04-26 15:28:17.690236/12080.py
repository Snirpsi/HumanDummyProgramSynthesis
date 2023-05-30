#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports. """    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    httpd = HTTPServer(("", 80), Handler)
    
    for port in ports:
        httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='./server.key', certfile='./server.crt')
        httpd.serve_forever()
        
    httpd.socket.close()
    httpd.server_close()
    
