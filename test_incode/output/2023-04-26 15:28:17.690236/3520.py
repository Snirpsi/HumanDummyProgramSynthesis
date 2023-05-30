#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits or enumerates user input. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('localhost', port), FruitServer)
    httpd.serve_forever()
    
