#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports and opens words. """    
    
    ports = [int(p) for p in sys.argv[1:]]
    
    httpd = HTTPServer(('', ports[0]), WordsHandler)
    httpd.serve_forever()
    
    
