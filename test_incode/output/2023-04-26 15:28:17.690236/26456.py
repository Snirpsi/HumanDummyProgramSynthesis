#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers and calculates fruits. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), FruitCalculator)
    
    print('Serving on port ' + str(port))
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nExiting...')
        server.socket.close()
        sys.exit(0)
    
