#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port or adds a list of numbers. """    
    port = int(sys.argv[1]) if len(sys.argv) > 1 else '8080'
    numbers = sys.argv[2:] if len(sys.argv) > 2 else None
    
    httpd = make_server('', port, Handler)
    httpd.serve_forever()
