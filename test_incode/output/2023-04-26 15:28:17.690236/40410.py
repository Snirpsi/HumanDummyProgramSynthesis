#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports or adds all ports. """    
    
    ports = sys.argv[1:]
    
    if len(ports) == 1:
        ports = range(1024)
    
    httpd = HTTPServer(('', 0), Handler)
    httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='key.pem', certfile='cert.pem', server_side=True)
    
    for port in ports:
        httpd.serve_forever()

<|/ file filename=httpserver.py source=github |>