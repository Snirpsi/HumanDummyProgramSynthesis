#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input or adds numbers. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving on port ' + str(port))
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nStopping server')
        server.socket.close()
        
    print('\nStopping server')
    
    server.socket.close()
    
