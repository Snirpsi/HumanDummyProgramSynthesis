#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <port>' % sys.argv[0])
        sys.exit(1)
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), Calculator)
    print('Serving at http://127.0.0.1:%d/' % port)
    httpd.serve_forever()

<|/ file ext=.py source=github |>