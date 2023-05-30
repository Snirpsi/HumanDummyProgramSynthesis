#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), MyHandler)
    
    print('Serving on port %s' % port)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nStopping...')
        server.socket.close()
        
    print('Stopped.')

