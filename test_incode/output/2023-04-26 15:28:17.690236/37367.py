#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port and removes a list of words. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), WordsHandler)
    httpd.serve_forever()
    
