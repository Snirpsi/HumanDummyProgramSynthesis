#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitHandler)
    print('Serving at http://127.0.0.1:%d/' % port)
    httpd.serve_forever()
    
