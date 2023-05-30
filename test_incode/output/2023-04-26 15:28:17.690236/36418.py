#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits. """    
    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, FruitHandler)
    httpd.serve_forever()
