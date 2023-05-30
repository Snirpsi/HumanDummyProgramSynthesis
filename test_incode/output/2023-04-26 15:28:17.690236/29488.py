#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts all ports. """    
    ports = [8080, 8081, 8082]
    
    for port in ports:
        server = HTTPServer(('', port), Handler)
        server.serve_forever()
