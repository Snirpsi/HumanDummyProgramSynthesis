#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers or converts a list of numbers. """    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: python -m webserver [port]")
        sys.exit(1)
    
    port = int(sys.argv[1])
    
    httpd = make_server("", port, Site)
    httpd.serve_forever()
    
