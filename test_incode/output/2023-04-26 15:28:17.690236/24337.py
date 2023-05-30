#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s [port]' % sys.argv[0])
        sys.exit()
    
    port = sys.argv[1]
    
    httpd = HTTPServer(('localhost', port), FruitHandler)
    print('Serving at http://127.0.0.1:%s' % port)
    httpd.serve_forever()
    
