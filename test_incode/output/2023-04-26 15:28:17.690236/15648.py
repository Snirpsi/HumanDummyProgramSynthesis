#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words. """    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
        
    httpd = HTTPServer(('', int(port)), WordsHandler)
    httpd.serve_forever()
    
