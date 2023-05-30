#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports and adds numbers. """    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    ports_str = ','.join(map(str, ports))
    
    server = HTTPServer(('', 8080), Handler)
    server.serve_forever()
    
