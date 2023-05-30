#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input or prints a list of numbers. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), MyHandler)
    print('Serving on port %s' % port)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nStopping server')
        server.socket.close()
        
    print('\nStopping server')
    server.socket.close()
    
