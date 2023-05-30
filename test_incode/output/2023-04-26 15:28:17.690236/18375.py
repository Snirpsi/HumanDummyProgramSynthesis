#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words. """    
    
    import sys
    
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    words.sort()
    
    port = 8000
    
    httpd = HTTPServer(('', port), WordsHandler)
    httpd.serve_forever()
    
