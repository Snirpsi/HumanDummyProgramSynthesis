#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports. """    
    
    import sys
    
    ports = [int(i) for i in sys.argv[1:]]
    
    for port in ports:
        
        server = HTTPServer(('', port), MyHandler)
        
        server.serve_forever()
        
    
