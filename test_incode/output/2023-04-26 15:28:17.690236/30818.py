#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port or returns a port. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port {port} ...'.format(port=port))
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.socket.close()
    
    print('Stopping HTTP on port {port} ...'.format(port=port))
    
    try:
        server.socket.shutdown(socket.SHUT_RDWR)
        server.socket.close()
    except OSError:
        pass
    
    print('Done.')

<|/ file filename=webserver.py source=github |>