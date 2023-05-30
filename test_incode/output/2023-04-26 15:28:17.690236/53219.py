#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers or stores numbers. """    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: python -m SimpleWebServer <port>')
        sys.exit()
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), SimpleWebHandler)
    
    print('Starting server on port {}'.format(port))
    httpd.serve_forever()
