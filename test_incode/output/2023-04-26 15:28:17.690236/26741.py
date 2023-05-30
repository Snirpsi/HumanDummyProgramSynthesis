#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words and returns a port. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), WordsServer)
    httpd.serve_forever()
    
