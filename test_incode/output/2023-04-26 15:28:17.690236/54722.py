#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port and iterates over user input. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), Handler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()
        
