#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits and removes numbers. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), FruitHandler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()
        
