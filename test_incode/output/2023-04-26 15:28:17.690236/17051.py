#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers or prints numbers. """    
    
    port = int(sys.argv[1])
    
    web = HTTPServer(('', port), SimpleHTTPRequestHandler)
    web.serve_forever()
    
