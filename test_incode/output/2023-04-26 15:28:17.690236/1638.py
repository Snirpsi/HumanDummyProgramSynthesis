#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers and returns all ports. """    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='server.key', certfile='server.crt')
    
    for port in ports:
        httpd.serve_forever()
        
    httpd.socket.close()
    httpd.server_close()
    
    print('Server shut down.')
    
