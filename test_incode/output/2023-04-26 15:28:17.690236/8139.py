#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers. """    
    import sys
    port = int(sys.argv[1])
    
    numbers = [int(i) for i in sys.argv[2:]]
    
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    for n in numbers:
        server.handle_request()
    
    server.socket.close()
    
    print('Server shut down')
    
