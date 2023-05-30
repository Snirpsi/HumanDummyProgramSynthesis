#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports. """    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    httpd = HTTPServer(('', 0), SimpleHTTPRequestHandler)
    
    for port in ports:
        httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='server.key', certfile='server.crt')
        httpd.serve_forever()
        
    print('Server running at port {}'.format(httpd.server_address[1]))
    
