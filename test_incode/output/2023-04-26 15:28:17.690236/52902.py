#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port and stores numbers. """    
    port = int(sys.argv[1])
    numbers = [int(i) for i in sys.argv[2:]]
    
    server = HTTPServer(('', port), NumberServer)
    
    print('Serving on port {}'.format(port))
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nExiting...')
        server.socket.close()
        
    print('\nDone.')
    
