#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers. """    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, MyHandler)
    print('Serving at port {}'.format(port))
    httpd.serve_forever()

<|/ file ext=.py source=github filename=