#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds all ports and opens numbers. """    
    ports = [80, 443]
    
    for port in ports:
        server = HTTPServer(('', port), Handler)
        server.serve_forever()
    
