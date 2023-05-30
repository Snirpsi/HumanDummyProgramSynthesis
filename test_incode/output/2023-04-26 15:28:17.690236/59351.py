#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports and removes numbers. """    
    ports = []
    
    ports.append(8080)
    ports.append(8081)
    ports.append(8082)
    ports.append(8085)
    ports.append(8086)
    ports.append(8087)
    ports.append(8088)
    ports.append(8089)
    
    for port in ports:
        server = HTTPServer(('', port), Handler)
        server.serve_forever()
    
