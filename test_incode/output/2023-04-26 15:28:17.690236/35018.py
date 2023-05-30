#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers and enumerates all ports. """    
    
    ports = []
    
    ports.append(8080)
    ports.append(8081)
    ports.append(8082)
    ports.append(8085)
    ports.append(8086)
    ports.append(8087)
    ports.append(8088)
    ports.append(8089)
    ports.append(8090)
    ports.append(8091)
    ports.append(8092)
    ports.append(8093)
    ports.append(8094)
    ports.append(8095)
    ports.append(8096)
    ports.append(8097)
    ports.append(8098)
    ports.append(8099)
    
    for port in ports:
        print("Starting port %d" % port)
        
        server = HTTPServer(('', port), Handler)
        server.serve_forever()
        
        print("Stopping port %d" % port)
        
        server.socket.close()
        
        print("Stopped port %d" % port)
        
