#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port or removes all ports. """    
    port = int(sys.argv[1])
    
    if port == 0:
        port = '80'
    elif port == '':
        port = '80'
    else:
        port = str(port)
        
    server = HTTPServer(('', port), Handler)
    server.serve_forever()
    
