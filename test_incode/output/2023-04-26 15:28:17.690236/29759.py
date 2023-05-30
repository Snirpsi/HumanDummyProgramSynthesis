#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports. """    
    
    ports = []
    
    server = HTTPServer(('', 0), Handler)
    server.serve_forever()
    
    ports.append(server.socket.getsockname()[1])
    
    
