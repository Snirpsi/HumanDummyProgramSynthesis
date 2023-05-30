#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words. """    
    
    import sys
    
    words = ['the', 'cat', 'is', 'a', 'cat']
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()
    
