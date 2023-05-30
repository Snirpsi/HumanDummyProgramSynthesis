#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit()
    
    words = [word.strip() for word in sys.argv[1].split(',')]
    
    httpd = HTTPServer(('', 8000), MyHandler)
    httpd.serve_forever()
    
