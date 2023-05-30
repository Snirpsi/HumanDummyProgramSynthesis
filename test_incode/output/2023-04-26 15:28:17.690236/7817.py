#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    
    words = []
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('localhost', port), WordsHandler)
    
    httpd.serve_forever()
    
