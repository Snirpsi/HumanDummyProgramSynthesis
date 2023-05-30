#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers and enumerates all ports. """    
    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    for port in ports:
        
        server = HTTPServer(('', port), Handler)
        server.serve_forever()
        
    print('Server running at port %s' % port)

<|/ file source=github filename=webserver.py |>