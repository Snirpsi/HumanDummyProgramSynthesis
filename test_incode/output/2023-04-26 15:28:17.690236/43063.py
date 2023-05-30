#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words and converts a port. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), WordsHandler)
    httpd.serve_forever()
    
