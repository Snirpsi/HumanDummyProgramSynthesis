#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port. """    
    port = 8080
    httpd = HTTPServer(('', port), MyHandler)
    print('Serving on port {}'.format(port))
    httpd.serve_forever()
