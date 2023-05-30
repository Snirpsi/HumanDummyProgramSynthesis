#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports and returns user input. """    
    ports = range(1,65535)
    
    for port in ports:
        server = HTTPServer(('localhost', port), Handler)
        print('Serving on port {}'.format(port))
        server.serve_forever()
    
