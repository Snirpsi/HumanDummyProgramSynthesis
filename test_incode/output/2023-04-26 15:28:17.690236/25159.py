#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitServer)
    print('Serving at port %s' % port)
    httpd.serve_forever()
    
