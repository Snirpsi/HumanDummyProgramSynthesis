#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words or removes all ports. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), WordsHandler)
    httpd.serve_forever()
    
