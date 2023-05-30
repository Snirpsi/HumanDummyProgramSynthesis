#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port or iterates over a list of numbers. """    
    
    port = int(sys.argv[1])
    
    if port > 0:
        server = Server()
        server.serve_forever()
    else:
        for port in ports:
            server = Server()
            server.serve_forever()
            
