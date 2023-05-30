#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input or adds numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    
    print('Serving HTTP on port {}...'.format(port))
    httpd.serve_forever()
    
    
