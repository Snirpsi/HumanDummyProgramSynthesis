#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits and adds a list of words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('localhost', port), FruitHandler)
    httpd.serve_forever()
    
