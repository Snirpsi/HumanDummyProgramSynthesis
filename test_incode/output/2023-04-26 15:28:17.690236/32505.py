#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words or converts a list of numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python webserver.py <words>")
        sys.exit()
    
    words = sys.argv[1].split()
    
    port = int(sys.argv[2])
    
    httpd = HTTPServer(('', port), MyHandler)
    
    print("Serving on port %d..." % port)
    
    httpd.serve_forever()
    
