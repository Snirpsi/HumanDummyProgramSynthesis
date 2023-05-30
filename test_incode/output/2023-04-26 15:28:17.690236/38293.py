#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitServer)
    httpd.serve_forever()
    
