#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers or converts all ports. """    
    
    ports = [8080, 8081, 8082]
    
    for port in ports:
        httpd = make_server(port, "", make_httpd)
        httpd.serve_forever()
        
