#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), RemoveWords)
    httpd.serve_forever()
    
