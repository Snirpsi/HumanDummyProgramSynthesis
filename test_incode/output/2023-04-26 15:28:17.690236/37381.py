#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers and prints words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit(1)
    
    port = sys.argv[1]
    
    httpd = HTTPServer(('', port), WordsHandler)
    httpd.serve_forever()
    
