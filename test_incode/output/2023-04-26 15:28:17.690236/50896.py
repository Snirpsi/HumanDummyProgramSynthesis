#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port or adds words. """    
    port = int(sys.argv[1])
    
    words = ['hello', 'world']
    
    httpd = HTTPServer(('', port), WordsHandler)
    httpd.serve_forever()
    
