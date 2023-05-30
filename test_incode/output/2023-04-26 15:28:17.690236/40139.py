#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input and converts fruits. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitConverter)
    print('Serving at port {}'.format(port))
    httpd.serve_forever()
    
