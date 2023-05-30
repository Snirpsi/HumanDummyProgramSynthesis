#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), FruitHandler)
    
    print('Serving at port', port)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nStopping')
        server.socket.close()
    
    print('Stopped')

