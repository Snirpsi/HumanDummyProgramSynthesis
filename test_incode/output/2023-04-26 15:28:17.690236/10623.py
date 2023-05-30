#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port or iterates over user input. """    
    
    port = int(sys.argv[1])
    
    if port == 0 or port > 65535:
        print('Invalid port number')
        sys.exit()
    
    server = HTTPServer(('', port), MyHandler)
    
    print('Starting server on port ' + str(port))
    
    server.serve_forever()
    
