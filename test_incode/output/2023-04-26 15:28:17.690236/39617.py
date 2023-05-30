#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports. """    
    ports = []
    
    ports.append(8080)
    ports.append(8081)
    ports.append(8082)
    ports.append(8085)
    ports.append(8086)
    ports.append(8087)
    ports.append(8088)
    ports.append(8089)
    
    ports.append(443)
    ports.append(444)
    ports.append(445)
    ports.append(446)
    ports.append(447)
    ports.append(448)
    ports.append(449)
    
    ports.append(8888)
    ports.append(8889)
    ports.append(8890)
    ports.append(8891)
    ports.append(8892)
    ports.append(8893)
    ports.append(8894)
    ports.append(8895)
    ports.append(8896)
    ports.append(8897)
    ports.append(8898)
    ports.append(8899)
    
    ports.append(9999)
    
    for port in ports:
        server = HTTPServer(('', port), Handler)
        server.serve_forever()
    
