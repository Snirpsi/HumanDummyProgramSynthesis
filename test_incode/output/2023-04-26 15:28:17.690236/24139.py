#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports. """    
    ports = []
    
    for port in range(8000, 9001):
        ports.append(port)
    
    print('Available ports: {}'.format(ports))
    
    httpd = HTTPServer(("", ports[0]), MyHandler)
    print('Serving on port {}'.format(ports[0]))
    httpd.serve_forever()
    
