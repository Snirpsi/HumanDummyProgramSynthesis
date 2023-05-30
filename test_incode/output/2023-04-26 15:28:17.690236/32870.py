#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), MyHandler)
    
    print('Serving on port {}'.format(port))
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nExiting')
        server.socket.close()
        sys.exit(0)
    
    server.socket.close()
    
