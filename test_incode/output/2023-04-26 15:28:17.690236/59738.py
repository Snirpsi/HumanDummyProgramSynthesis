#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 5000
    
    httpd = HTTPServer(('', port), WordCalculator)
    print('Starting httpserver on port %s' % port)
    httpd.serve_forever()

<|/ file source=github |>