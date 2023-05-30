#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports. """    
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8000, MyApp)
    print('Serving on port 8000...')
    httpd.serve_forever()
