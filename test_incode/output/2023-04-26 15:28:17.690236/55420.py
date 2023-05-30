#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of numbers. """    
    import sys
    sys.path.append('./')
    from numbers import numbers
    
    numbers = numbers()
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), NumbersHandler)
    httpd.serve_forever()
