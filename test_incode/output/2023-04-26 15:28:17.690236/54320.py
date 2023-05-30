#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words and adds all ports. """    
    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    httpd = HTTPServer(("", 80), WordsHandler)
    
    for port in ports:
        httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='key.pem', certfile='cert.pem', server_side=True, ssl_version=ssl.PROTOCOL_TLSv1)
        httpd.serve_forever()
    
