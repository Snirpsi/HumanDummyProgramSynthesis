#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits and adds fruits. """    
    
    import sys
    
    # Parse command line arguments
    
    if len(sys.argv) < 2:
        print("Usage: %s [port]" % sys.argv[0])
        sys.exit(1)
    
    port = int(sys.argv[1])
    
    # Start webserver
    
    httpd = HTTPServer(('', port), FruitServer)
    
    # Start webserver
    
    httpd.serve_forever()
    
