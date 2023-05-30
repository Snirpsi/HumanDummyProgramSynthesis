#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words or converts all ports. """    
    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    webserver = WebServer()
    webserver.listen(ports)
    
    webserver.serve_forever()
