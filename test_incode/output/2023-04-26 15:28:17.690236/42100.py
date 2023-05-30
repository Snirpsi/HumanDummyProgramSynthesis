#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), FruitHandler)
    
    print('Serving at http://127.0.0.1:{}/'.format(port))
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nStopping...')
        server.socket.close()
        server.server_close()
        
