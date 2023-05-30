#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words. """    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('localhost', port), WordsHandler)
    httpd.serve_forever()
