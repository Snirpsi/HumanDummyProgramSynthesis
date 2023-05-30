#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits and adds words. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitHandler)
    print('Serving at port %s' % port)
    httpd.serve_forever()
    
