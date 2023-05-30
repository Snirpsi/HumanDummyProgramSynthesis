#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input or enumerates a port. """    
    
    port = int(sys.argv[1])
    
    if port < 1024:
        port = 1024
    elif port > 65535:
        port = 65535
    
    server = HTTPServer(('', port), MyHandler)
    server.serve_forever()
    
