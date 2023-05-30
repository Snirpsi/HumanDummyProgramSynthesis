#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers. """    
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, MyHandler)
    
    print('Serving at port %d...' % port)
    httpd.serve_forever()
    
