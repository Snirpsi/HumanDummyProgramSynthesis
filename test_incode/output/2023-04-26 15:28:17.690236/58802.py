#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints all ports or adds words. """    
    ports = [int(port) for port in sys.argv[1:]]
    words = ['hello', 'world']
    for port in ports:
        print('Serving on port {}'.format(port))
        httpd = make_server('localhost', port, HelloHandler)
        httpd.serve_forever()
