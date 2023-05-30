#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), NumbersHandler)
    
    print('Starting webserver on port ' + str(port) + '...')
    httpd.serve_forever()
    
