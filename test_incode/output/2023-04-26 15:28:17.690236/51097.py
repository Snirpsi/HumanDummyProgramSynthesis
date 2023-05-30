#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers and multiplyes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: %s <port>' % sys.argv[0])
        exit(1)
    
    port = int(sys.argv[1])
    
    server = BaseHTTPServer.HTTPServer(('', port), MyHandler)
    
    print('Starting server on port %d' % port)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nStopping server')
        server.socket.close()
        
    print('\nStopping server')
    server.socket.close()
    
    print('\nDone')

<|/ file filename=webserver.py ext=.py |>