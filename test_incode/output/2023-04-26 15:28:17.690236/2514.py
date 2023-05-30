#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    web = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
    web.serve_forever()
