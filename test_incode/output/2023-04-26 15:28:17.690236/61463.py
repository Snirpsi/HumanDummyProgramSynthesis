#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports. """    
    
    ports = [8080, 8081, 8082]
    
    for port in ports:
        httpd = make_server(port, app, debug=True)
        httpd.serve_forever()
        
    
