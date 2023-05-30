#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words or adds a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        host = sys.argv[1]
        
        port = int(sys.argv[2])
        
        webserver = HTTPServer(
            (host, port),
            SimpleHTTPRequestHandler
        )
        
        webserver.serve_forever()
    else:
        
        webserver = HTTPServer(
            ('', 8080),
            SimpleHTTPRequestHandler
        )
        
        webserver.serve_forever()
    
