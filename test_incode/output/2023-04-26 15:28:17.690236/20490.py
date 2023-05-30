#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports and adds numbers. """    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    ports_str = []
    for port in ports:
        ports_str.append(str(port))
    
    ports_str = ", ".join(ports_str)
    
    httpd = HTTPServer(('', 8080), Handler)
    httpd.serve_forever()
    
