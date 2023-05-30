#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes user input and opens all ports. """    
    
    ports = [8080, 8081, 8082]
    
    httpd = HTTPServer(('', 0), SimpleHTTPRequestHandler)
    
    for port in ports:
        httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='server.key', certfile='server.crt', server_side=True)
        httpd.serve_forever()
        
