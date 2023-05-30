#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words or enumerates all ports. """    
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, MyHandler)
    
    print('Starting web server on port ' + str(port))
    httpd.serve_forever()
    
