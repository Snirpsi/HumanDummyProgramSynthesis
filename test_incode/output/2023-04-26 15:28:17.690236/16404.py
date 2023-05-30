#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers or converts user input. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    
    print('Serving HTTP on port {port} ...'.format(port=port))
    httpd.serve_forever()
    
