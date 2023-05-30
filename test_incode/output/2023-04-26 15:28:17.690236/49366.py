#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), NumberHandler)
    
    print('Serving at port {port}'.format(port=port))
    
    httpd.serve_forever()
    
