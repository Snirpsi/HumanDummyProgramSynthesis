#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers or removes words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8080
    
    httpd = HTTPServer(('', port), MyHandler)
    print('Serving at port %s' % port)
    httpd.serve_forever()
    
