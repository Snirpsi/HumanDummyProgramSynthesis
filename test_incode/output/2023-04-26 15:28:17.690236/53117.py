#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = make_server('', port, MyHandler)
    
    print('Serving at http://127.0.0.1:{}/'.format(port))
    
    httpd.serve_forever()
    
