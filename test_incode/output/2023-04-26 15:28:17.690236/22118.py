#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers or iterates over numbers. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), NumberCalculator)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.socket.close()
    
