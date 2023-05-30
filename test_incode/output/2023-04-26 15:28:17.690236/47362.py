#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits or converts words. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitHandler)
    print('Serving at http://127.0.0.1:{}/'.format(port))
    httpd.serve_forever()
    
