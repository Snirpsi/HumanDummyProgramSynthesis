#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = 8000
    
    httpd = make_server('', port, FruitHandler)
    
    print('Serving at port', port)
    httpd.serve_forever()
