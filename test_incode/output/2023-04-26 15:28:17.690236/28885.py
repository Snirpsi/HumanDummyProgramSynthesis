#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports and prints words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    server = None
    
    try:
        server = HTTPServer(('', port), MyHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    if server:
        server.socket.close()
        
