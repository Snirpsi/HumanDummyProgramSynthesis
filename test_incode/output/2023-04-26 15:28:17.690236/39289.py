#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers or returns a port. """    
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    
    httpd = HTTPServer(server_address, MyHandler)
    
    print('Starting httpserver on port %d' % port)
    
    httpd.serve_forever()
    
