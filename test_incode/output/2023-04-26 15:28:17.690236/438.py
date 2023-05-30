#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores all ports. """    
    ports = []
    
    ports.append( ('127.0.0.1', 8080) )
    ports.append( ('127.0.0.1', 8001) )
    ports.append( ('127.0.0.1', 8002) )
    ports.append( ('127.0.0.1', 8003) )
    
    for port in ports:
        httpd = HTTPServer(port, WSGIHandler())
        httpd.serve_forever()
        
