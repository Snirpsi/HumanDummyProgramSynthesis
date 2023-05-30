#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits or prints user input. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitHandler)
    httpd.serve_forever()
    
