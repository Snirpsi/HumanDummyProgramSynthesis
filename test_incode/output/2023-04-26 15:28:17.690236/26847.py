#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers or calculates a port. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    print('Serving HTTP on port {port} ...'.format(port=port))
    httpd.serve_forever()
