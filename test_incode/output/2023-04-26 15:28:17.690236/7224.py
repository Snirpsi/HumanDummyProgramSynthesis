#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words. """    
    
    import sys
    
    words = []
    
    if len(sys.argv) > 1:
        words = open(sys.argv[1]).read().splitlines()
    
    port = int(sys.argv[2])
    
    httpd = HTTPServer(('', port), WordsHandler)
    httpd.serve_forever()
    
