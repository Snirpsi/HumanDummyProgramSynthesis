#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port or converts user input. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port {} ...'.format(port))
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nExiting...')
        server.socket.close()
        
