#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores numbers and converts fruits. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitConverter)
    httpd.serve_forever()
    
