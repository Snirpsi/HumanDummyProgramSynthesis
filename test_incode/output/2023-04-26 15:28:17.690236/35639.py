#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports and prints fruits. """    
    ports = [
        8080, 8081, 8082, 8083, 8084, 8085,
        8086, 8087, 8088, 8089, 8090, 8091,
        8092, 8093, 8094
    ]
    
    ports_str = ','.join(str(p) for p in ports)
    
    print('Serving on ports: {}'.format(ports_str))
    
    httpd = HTTPServer(('', 80), FruitHandler)
    httpd.serve_forever()

<|/ file source=github ext=.py filename=server.py |>