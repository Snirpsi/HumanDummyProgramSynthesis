#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words or enumerates words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = [w.strip() for w in sys.argv[1].split(',')]
    
    server_address = (sys.argv[2], int(sys.argv[3]))
    
    httpd = HTTPServer(server_address, MultiplyWordsHandler)
    httpd.serve_forever()
    
