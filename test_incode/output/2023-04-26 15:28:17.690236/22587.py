#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words. """    
    
    import sys
    
    words = ['word1', 'word2', 'word3', 'word4']
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    print('Serving HTTP on port {} ...'.format(port))
    
    httpd.serve_forever()
    
