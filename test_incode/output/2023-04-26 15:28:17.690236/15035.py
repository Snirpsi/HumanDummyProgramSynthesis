#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers. """    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    httpd = make_server('', port, MyHandler)
    print('Serving at http://%s:%d/' % server_address)
    httpd.serve_forever()
