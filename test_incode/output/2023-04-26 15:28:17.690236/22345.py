#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports. """    
    from wsgiref.simple_server import make_server
    
    httpd = make_server('localhost', 8000, MyHandler)
    print('Serving on port 8000...')
    httpd.serve_forever()
