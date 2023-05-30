#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words or returns fruits. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), WordsHandler)
    httpd.serve_forever()
    
