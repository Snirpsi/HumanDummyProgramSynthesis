#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port and converts words. """    
    port = int(sys.argv[1])
    
    words = ['hello', 'world', '!']
    
    httpd = HTTPServer(('', port), WordsHandler)
    httpd.serve_forever()
    
